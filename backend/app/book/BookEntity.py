from sqlalchemy import Column, Integer, String, Date
from backend.database import Base


class BookEntity(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    authors = Column(String(255), nullable=True)
    publisher = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    date = Column(Date, nullable=True)
    isbn = Column(String(255), nullable=True)
    pages = Column(Integer, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "publisher": self.publisher,
            "category": self.category,
            "date": self.date.isoformat() if self.date else None,
            "isbn": self.isbn,
            "pages": self.pages
        }

    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(
            title=data["title"],
            authors=data.get("authors") if "authors" in data else None,
            isbn=data.get("isbn")if "isbn" in data else None,
            publisher=data.get("publisher")if "publisher" in data else None,
            category=data.get("category")if "category" in data else None,
            date=data.get("date")if "date" in data else None,
            pages=data.get("pages")if "pages" in data else None
        )