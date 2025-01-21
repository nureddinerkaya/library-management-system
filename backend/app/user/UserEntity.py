from datetime import date

from dateutil.relativedelta import relativedelta
from sqlalchemy import Column, Integer, String, Date
from backend.database import Base


class UserEntity(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String)
    signupDate = Column(Date, nullable=False)
    renevalDate = Column(Date)
    expirationDate = Column(Date)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "type": self.type,
            "phone": self.phone,
            "email": self.email,
            "signupDate": self.signupDate.isoformat() if self.signupDate else None,
            "renevalDate": self.renevalDate.isoformat() if self.renevalDate else None,
            "expirationDate": self.expirationDate.isoformat() if self.expirationDate else None,
        }

    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(
            username=data["username"],
            name=data["name"],
            password=data["password"],
            type=data["type"],
            phone=data["phone"],
            email=data["email"] if "email" in data else None,
            signupDate=data.get("signupDate", date.today()),  # Use current date if not provided
            renevalDate=data["renevalDate"] if "renevalDate" in data else None,
            expirationDate=(data.get("signupDate", date.today()) + relativedelta(years=1)),
        )

#    @classmethod
#    def put_from_dict(cls, data):
#        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
#        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
#        return cls(
#            username=data["username"],
#            name=data["name"],
#            password=data["password"],
#            type=data["type"],
#            phone=data["phone"],
#            email=data["email"],
#            signupDate=data["signupDate"],
#            renevalDate=data["renevalDate"] if "renevalDate" in data else None,
#            expirationDate=(
#                data["renevalDate"] + relativedelta(years=1)
#                if "renevalDate" in data and data["renevalDate"]
#                else None
#            ),
#        )