from sqlalchemy import Column, Integer, String, Date, ForeignKey
from backend.database import Base
from backend.app.copies.Copies import Copies
from sqlalchemy.orm import relationship
from backend.app.user.UserEntity import UserEntity


class BorrowingEntity(Base):
    __tablename__ = "Borrowing"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    copy = Column(Integer,ForeignKey(Copies.id), nullable=False)
    member = Column(Integer,ForeignKey(UserEntity.id), nullable=False)
    borrow_date = Column(Date, nullable=False)
    expected_date = Column(Date, nullable=True)
    return_date = Column(Date, nullable=True)
    state = Column(String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "copy": self.copy,
            "member": self.member,
            "borrow_date": self.borrow_date.isoformat(),
            "expected_date": self.expected_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None,
            "state":self.state

        }

    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(

            copy=data.get("copy"),
            member=data.get("member"),
            borrow_date=data.get("borrow_date"),
            expected_date=data.get("expected_date"),
            return_date=data.get("return_date"),
            state="pending"

        )