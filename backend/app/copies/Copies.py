from sqlalchemy import Column, Integer, ForeignKey, String, Date, CHAR
from sqlalchemy.orm import relationship
from backend.database import Base
from backend.app.book.BookEntity import BookEntity


class Copies(Base):
    __tablename__ = 'Copies'  # Changed to plural for readability

    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    book = Column(Integer, ForeignKey(BookEntity.id), nullable=False)
    print_no = Column(Integer, nullable=False)
    location = Column(Integer, nullable=False)  # Nullable values should be explicit
    availability = Column(String(5), nullable=False)
    addition_date = Column(Date, nullable=False)
    removal_date = Column(Date, nullable=True)

    # Define relationship with BookEntity for ORM optimization


    def to_dict(self):
        return {
            "id": self.id,
            "book": self.book,
            "print_no": self.print_no,
            "location": self.location,
            "availability": self.availability,
            "addition_date": self.addition_date.isoformat() if self.addition_date else None,
            "removal_date": self.removal_date.isoformat() if self.removal_date else None,

        }

    @classmethod
    def from_dict(cls, data):
        # cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        return cls(

            book=data["book"],
            print_no=data["print_no"],
            location=data.get("location"),
            availability=data.get("availability"),
            addition_date=data.get("addition_date"),
            removal_date=data.get("removal_date"),

        )
