from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey
from websockets.http11 import Request

from backend.app.book.BookEntity import BookEntity
from backend.app.book.BookService import BookService
from backend.database import Base


class ImageEntity(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bookId = Column(Integer, ForeignKey(BookEntity.id), nullable=False)
    data = Column(LargeBinary, nullable=False)
    mime_type = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'bookId': self.bookId,
            'data': self.data,
            'mime_type': self.mime_type
        }

    @classmethod
    def from_dict(cls, request):
        file = request.files['file'][0]
        return cls(
            bookId=request.form.get('bookId'),
            data=file.body,
            mime_type=file.type
        )

