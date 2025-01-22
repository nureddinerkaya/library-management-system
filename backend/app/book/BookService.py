from sanic import json, text

from backend.app.book.BookEntity import BookEntity
from backend.database import SessionLocal


class BookService:

    @staticmethod
    async def get_all_books(request):
        with SessionLocal() as session:
            results = session.query(BookEntity).all()
            books = [book.to_dict() for book in results]
            return json(books)

    @staticmethod
    async def find_by_id(id):
        with SessionLocal() as session:
            book = session.query(BookEntity).filter(BookEntity.id == id).first()
            return book

    @staticmethod
    async def get_book_by_id(request):
        with SessionLocal() as session:
            try:
                book_id = int(request.args.get("id"))
                book = await BookService.find_by_id(book_id)
                if book:
                    result = book.to_dict()
                    return json(result)
                return json({"status": "error", "message": "BookEntity not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def add_book(request):
        with SessionLocal() as session:
            try:
                data = request.json #bu fonksiyon json payload'ını alıp python dict'ine dönüştürüyormuş
                new_book = BookEntity.from_dict(data)
                session.add(new_book)
                session.commit()
                return text("status: success, message" "BookEntity added successfully")
            except Exception as e:
                session.rollback()
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))
            finally:
                session.close()

    @staticmethod
    async def update_book(request):
        session = SessionLocal()
        try:
            data = request.json
            book_id = data["id"]
            book = session.query(BookEntity).filter_by(id=book_id).first()
            if not book:
                return text("BookEntity not found")

            for key, value in data.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            session.commit()
            return text("{)status: success, message: BookEntity updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()

    @staticmethod
    async def delete_book(request):
        session = SessionLocal()
        try:
            book_id = int(request.args.get("id"))
            book = session.query(BookEntity).filter_by(id=book_id).first()
            if not book:
                return json({"status": "error", "message": "BookEntity not found"})
            session.delete(book)
            session.commit()
            return json({"status": "success", "message": "BookEntity deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()


