from sqlalchemy import Column, Integer, ForeignKey, String, Date, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
from backend.app.book.BookEntity import BookEntity


class Copies(Base):
    __tablename__ = 'copies'  # Changed to plural for readability

    id = Column(Integer, primary_key=True, nullable=False)
    book = Column(Integer, ForeignKey(BookEntity.ID), nullable=False)
    print_no = Column(Integer, nullable=False)
    location = Column(Integer, nullable=False)  # Nullable values should be explicit
    availability = Column(String(1), nullable=False)
    addition_date = Column(Date, nullable=False)
    removal_date = Column(Date, nullable=False)

    # Define relationship with BookEntity for ORM optimization
    book_relationship = relationship("BookEntity", back_populates="copies")
