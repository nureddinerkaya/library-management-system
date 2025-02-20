from sqlalchemy.orm import Session
from sanic import json, text

from backend.app.book.BookService import BookService
from backend.app.book.BookEntity import BookEntity
from backend.app.borrowing.BorrowingBlueprint import get_book_by_title
from backend.app.copies.Copies import Copies
from backend.database import SessionLocal
from datetime import datetime





class CopiesServices:
    @staticmethod
    async def add_copy(request):
        session = SessionLocal()
        try:
            data = request.json
            new_copy = Copies.from_dict(data)
            session.add(new_copy)
            book=await BookService.find_by_id(data["book"])
            book.stock+=1
            session.add(book)
            session.commit()


            return json({"message": "Copy added successfully."})
        except Exception as e:
            session.rollback()
            return json({"error": f"Error adding copy: {str(e)}"})
        finally:
            session.close()



    @staticmethod
    async def view_copies(request):
        """
        Views the list of copies in the database.
        """
        with SessionLocal() as session:

           results = session.query(Copies).all()
           copies = [book.to_dict() for book in results]
           return json(copies)

    @staticmethod
    async def view_copies_by_book_title(request):
        book_title = request.args.get("title")


        with SessionLocal() as session:
            try:
                # Kitabı sorgula
                book = session.query(BookEntity).filter(
                    BookEntity.title.ilike(f"%{book_title}%")
                ).first()


                if not book:  # Kitap bulunamazsa hata döndür
                    return json({"error": f"No copy found with the title '{book_title}'."})

                # Kitap ID'si üzerinden Copy'leri sorgula
                copies = session.query(Copies).filter(
                    Copies.book == book.id
                ).all()

                if not copies:  # Copy yoksa hata döndür
                    return json({"error": f"No copies found for the book titled '{book_title}'."})

                # Copy'leri liste halinde döndür
                results = [copy.to_dict() for copy in copies]
                return json({"book_title": book.title, "copies": results})

            except Exception as e:
                return json({"error": f"An error occurred: {str(e)}"})
            finally:
                session.close()


    @staticmethod
    def get_book_id_by_title(title):
        with SessionLocal() as session:  # Veritabanı oturumunu başlat
            # Kitap başlığına göre kitabı sorgula
            book = session.query(BookEntity).filter(
                BookEntity.title.ilike(f"%{title}%")  # Büyük/küçük harf duyarsız arama
            ).first()

            if book:  # Eğer kitap bulunduysa ID'sini döndür
                return book.id
            else:  # Eğer kitap bulunamazsa None döndür
                return None

    @staticmethod
    async def view_copies_by_id(request):


          with SessionLocal() as session:
            try:
                copy_id = int(request.args.get("id"))
                book = session.query(Copies).filter_by(id=copy_id).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Copies not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})
    @staticmethod
    async def view_copies_by_print_no(request):

          with SessionLocal() as session:
            try:
                print_noo = int(request.args.get("print_no"))
                book = session.query(Copies).filter_by(print_no=print_noo).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Copies not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def view_copies_by_location(request):

          with SessionLocal() as session:
            try:
                locationn= int(request.args.get("location"))
                book = session.query(Copies).filter_by(location=locationn).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Copies not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})



    @staticmethod
    async def view_copies_by_availability(request):

          with SessionLocal() as session:
            try:
                availabilityy= str(request.args.get("availability"))
                book = session.query(Copies).filter_by(availability=availabilityy).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Copies not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def view_copies_by_additiondate(request):

        with SessionLocal() as session:
            try:
                addition_date_str= request.args.get("addition_date")
                addition_date = datetime.strptime(addition_date_str, "%Y-%m-%d").date()
                book = session.query(Copies).filter_by(addition_date=addition_date).first()
                if book:
                    result = book.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Copies not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def delete_copy(request):
        session = SessionLocal()
        try:
            copy_id = int(request.args.get("id"))
            copy =  session.query(Copies).filter_by(id=copy_id).first()
            if not copy:
                return json({"status": "error", "message": "Copy not found"})
            session.delete(copy)
            book_id= copy.book
            book = await BookService.find_by_id(book_id)
            book.stock -= 1
            session.add(book)
            session.commit()
            return json({"status": "success", "message": "Copy deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()

    @staticmethod
    async def update_copy(request):
        session = SessionLocal()
        try:
            data = request.json
            copy_id = data["id"]
            book = session.query(Copies).filter_by(id=copy_id).first()
            if not book:
                return text("Copy not found")

            for key, value in data.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            session.commit()
            return text("{status: success, message: Copy updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()