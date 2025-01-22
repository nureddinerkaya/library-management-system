from sqlalchemy import Column, Integer, String, LargeBinary

from backend.database import Base


class ImageEntity(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(LargeBinary, nullable=False)
    mime_type = Column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data,
            'mime_type': self.mime_type
        }

    @classmethod
    def from_dict(cls, request):
        file = request.files['file'][0]
        return cls(
            data=file.body,
            mime_type=file.type
        )

