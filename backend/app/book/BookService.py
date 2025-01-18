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
    async def get_book_by_id(request):
        with SessionLocal() as session:
            try:
                book_id = int(request.args.get("id"))
                book = session.query(BookEntity).filter_by(id=book_id).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "BookEntity not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    #@staticmethod
    #async def get_book_by_title(request):
    #    with SessionLocal() as session:
    #        try:
    #            title = request.args.get("title")
    #            book = session.query(BookEntity).filter_by(title=title).first()
    #            if book:
    #                result = book.to_dict()
    #                return json({"status": "success", "data": result})
    #            return json({"status": "error", "message": "BookEntity not found"})
    #        except Exception as e:
    #            return json({"status": "error", "message": str(e)})
#
    #@staticmethod
    #async def get_book_by_authors(request):
    #    with SessionLocal() as session:
    #        try:
    #            authors = request.args.get("authors")
    #            book = session.query(BookEntity).filter_by(authors=authors).first()
    #            if book:
    #                result = book.to_dict()
    #                return json({"status": "success", "data": result})
    #            return json({"status": "error", "message": "BookEntity not found"})
    #        except Exception as e:
    #            return json({"status": "error", "message": str(e)})
#
    #@staticmethod
    #async def get_book_by_publisher(request):
    #    with SessionLocal() as session:
    #        try:
    #            publisher = request.args.get("publisher")
    #            book = session.query(BookEntity).filter_by(publisher=publisher).first()
    #            if book:
    #                result = book.to_dict()
    #                return json({"status": "success", "data": result})
    #            return json({"status": "error", "message": "BookEntity not found"})
    #        except Exception as e:
    #            return json({"status": "error", "message": str(e)})
#
    #@staticmethod
    #async def get_book_by_category(request):
    #    with SessionLocal() as session:
    #        try:
    #            category = request.args.get("category")
    #            book = session.query(BookEntity).filter_by(category=category).first()
    #            if book:
    #                result = book.to_dict()
    #                return json({"status": "success", "data": result})
    #            return json({"status": "error", "message": "BookEntity not found"})
    #        except Exception as e:
    #            return json({"status": "error", "message": str(e)})
#
    #@staticmethod
    #async def get_book_by_isbn(request):
    #    with SessionLocal() as session:
    #        try:
    #            isbn = request.args.get("isbn")
    #            book = session.query(BookEntity).filter_by(isbn=isbn).first()
    #            if book:
    #                result = book.to_dict()
    #                return json({"status": "success", "data": result})
    #            return json({"status": "error", "message": "BookEntity not found"})
    #        except Exception as e:
    #            return json({"status": "error", "message": str(e)})

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


