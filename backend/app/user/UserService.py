from sanic import json, text

from backend.app.user.UserEntity import UserEntity
from backend.database import SessionLocal


class UserService:

    @staticmethod
    async def get_all_users(request):
        with SessionLocal() as session:
            results = session.query(UserEntity).all()
            users = [user.to_dict() for user in results]
            return json(users)

    @staticmethod
    async def find_by_id(id):
        with SessionLocal() as session:
            user = session.query(UserEntity).filter(UserEntity.id == id).first()
            return user

    @staticmethod
    async def get_user_by_id(request):
        with SessionLocal() as session:
            try:
                user_id = int(request.args.get("id"))
                user = UserService.find_by_id(id)
                if user:
                    result = user.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "UserEntity not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def add_user(request):
        with SessionLocal() as session:
            try:
                data = request.json #bu fonksiyon json payload'ını alıp python dict'ine dönüştürüyormuş
                new_user = UserEntity.from_dict(data)
                session.add(new_user)
                session.commit()
                return text("status: success, message" "UserEntity added successfully")
            except Exception as e:
                session.rollback()
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))
            finally:
                session.close()

    @staticmethod
    async def update_user(request):
        session = SessionLocal()
        try:
            data = request.json
            user_id = data["id"]
            user = session.query(UserEntity).filter_by(id=user_id).first()
            if not user:
                return text("UserEntity not found")

            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            return text("{)status: success, message: UserEntity updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()

    @staticmethod
    async def delete_user(request):
        session = SessionLocal()
        try:
            user_id = int(request.args.get("id"))
            user = session.query(UserEntity).filter_by(id=user_id).first()
            if not user:
                return json({"status": "error", "message": "UserEntity not found"})
            session.delete(user)
            session.commit()
            return json({"status": "success", "message": "UserEntity deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()


