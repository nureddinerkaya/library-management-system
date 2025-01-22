import hashlib
import os
from .AuthEntity import User
from database import async_session

async def register_user(username, password):
    salt = os.urandom(16)  # Rastgele bir salt değeri oluştur
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    user = User(username=username, password_hash=hashed_password.hex(), salt=salt.hex())  # 'salt' eklemek önemli
    async with database() as session:
        async with session.begin():
            session.add(user)
            await session.commit()

async def authenticate_user(username, password):
    async with database() as session:
        async with session.begin():
            user = await session.execute(
                session.query(User).filter_by(username=username)
            )
            user = user.scalars().first()
            if user:
                # Hash'i çözmek için salt ve hash'i birleştirerek doğrulama yapıyoruz
                salt = bytes.fromhex(user.salt)
                stored_password = bytes.fromhex(user.password_hash)
                hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
                if hashed_password == stored_password:
                    return user
            return None
