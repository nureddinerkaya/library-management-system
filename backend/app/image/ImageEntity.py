from sqlalchemy import Column, Integer, String, Date, LargeBinary

from backend.app.book.BookEntity import BookEntity
from backend.app.book.BookService import BookService
from backend.database import Base


class ImageEntity(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book = Column(BookEntity, nullable=False)
    data = Column(LargeBinary, nullable=False)
    mime_type = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'book': self.book.id,
            'data': self.data,
            'mime_type': self.mime_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            book=BookService.find_by_id(data['bookId']),
            data=data['data'],
            mime_type=data['mime_type']
        )

