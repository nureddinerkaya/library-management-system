from datetime import datetime, timedelta
from sanic import json
import jwt
import asyncio
from backend.app.user.UserEntity import UserEntity
from backend.app.auth.AuthEntity import AuthEntity
from backend.database import SessionLocal

class AuthService:

    @staticmethod
    async def login(request):
        """Kullanıcıyı doğrulamak ve oturum açmak."""
        with SessionLocal() as session:
            try:
                data = request.json
                username = data["username"]
                password = data["password"]

                user = session.query(UserEntity).filter(UserEntity.username == username).first()

                if not user:
                    return json({"status": "error", "message": "User not found"}, status=404)

                if user.password != password:
                    return json({"status": "error", "message": "Invalid password"}, status=401)

                type = user.type
                token = AuthService.generate_token(user.id)

                # Yeni AuthEntity kaydı
                new_session = AuthEntity(user_id=user.id, token=token, type=type)
                session.add(new_session)
                session.commit()

                # 15 dakika sonra token silme işlemini başlat
                asyncio.create_task(AuthService.delete_token_after_delay(token, 900))  # 900 saniye = 15 dakika

                return json({"status": "success", "token": token})

            except Exception as e:
                return json({"status": "error", "message": str(e)}, status=500)
            finally:
                session.close()

    @staticmethod
    def generate_token(user_id):
        """JWT token üretir."""
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(minutes=15),  # Token 15 dakika geçerli
        }
        return jwt.encode(payload, "some_salt_value", algorithm="HS256")

    @staticmethod
    async def delete_token_after_delay(token, delay):
        """Belirli bir süre sonra token'ı veritabanından siler."""
        await asyncio.sleep(delay)
        with SessionLocal() as session:
            try:
                session_entry = session.query(AuthEntity).filter_by(token=token).first()
                if session_entry:
                    session.delete(session_entry)
                    session.commit()
            except Exception as e:
                print(f"Error deleting token: {e}")
            finally:
                session.close()

    @staticmethod
    async def get_token_by_username(request):
        """Kullanıcı adıyla token alır."""
        with SessionLocal() as session:
            try:
                data = request.json
                username = data["username"]

                # Kullanıcıyı bul
                user = session.query(UserEntity).filter_by(username=username).first()
                if not user:
                    return json({"status": "error", "message": "User not found"}, status=404)

                # Kullanıcıya ait en son token'ı bul
                session_entry = session.query(AuthEntity).filter_by(user_id=user.id).order_by(AuthEntity.id.desc()).first()
                if not session_entry:
                    return json({"status": "error", "message": "No active token found"}, status=404)

                return json({"status": "success", "token": session_entry.token})

            except Exception as e:
                return json({"status": "error", "message": str(e)}, status=500)
            finally:
                session.close()
