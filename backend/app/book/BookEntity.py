from sqlalchemy import Column, Integer, String
from backend.database import Base


class BookEntity(Base):
    __tablename__ = "Book"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    authors = Column(String(255), nullable=False, comment="A book can have multiple authors, consider using a list-like structure.")
    category = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    ISBN = Column(String(255), nullable=False)
    pages = Column(Integer, nullable=False)