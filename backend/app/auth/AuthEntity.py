from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class AuthEntity(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Kullanıcı ile ilişki
    token = Column(String, nullable=False, unique=True)  # Kullanıcıya özel oturum token'ı
    created_at = Column(DateTime, default=datetime.utcnow)  # Oturumun oluşturulma tarihi

    # User tablosuyla ilişki
    user = relationship("UserEntity", back_populates="sessions")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data["user_id"],
            token=data["token"],
            created_at=data.get("created_at", datetime.utcnow())
        )
