from sanic import json, text
from backend.app.borrowing.BorrowingEntity import BorrowingEntity
from backend.app.user.UserEntity import UserEntity
from backend.app.copies.Copies import Copies
from backend.database import SessionLocal
from sqlalchemy.orm import Session
from sanic import json, text


from backend.app.copies.Copies import Copies

from datetime import datetime

class BorrowingService:

    @staticmethod
    async def get_all_borrowings(request):
        with SessionLocal() as session:
            results = session.query(BorrowingEntity).all()
            records = [book.to_dict() for book in results]
            return json(records)


    @staticmethod
    async def get_borrowing_whose_are_pending(request):
        with SessionLocal() as session:
            try:
                results = session.query(BorrowingEntity).filter(BorrowingEntity.state.ilike("pending")).all()
                if results:
                    records = [record.to_dict() for record in results]
                    return json({"status": "success", "data": records})
                return json({"status": "error", "message": "No pending borrowings found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_whose_are_active(request):
        with SessionLocal() as session:
            try:
                results =  session.query(BorrowingEntity).filter(BorrowingEntity.state.ilike("Active")).all()
                if results:
                    records = [record.to_dict() for record in results]
                    return json({"status": "success", "data": records})
                return json({"status": "error", "message": "No active borrowings found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_whose_are_returned(request):
        with SessionLocal() as session:
            try:
                results = session.query(BorrowingEntity).filter(BorrowingEntity.state.ilike("Returned")).all()
                if results:
                    records = [record.to_dict() for record in results]
                    return json({"status": "success", "data": records})
                return json({"status": "error", "message": "No returned borrowings found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    #EXPECTED DATE GEÇMİŞ AMA STATE RETURNED OLMAMIŞ.
    #BU METOD HER ÇAĞIRILDIĞINDA BUNLARIDA KONTROL EDİYORUZ

    @staticmethod
    async def get_borrowing_whose_are_overdue(request):
        with SessionLocal() as session:
            try:
                await BorrowingService.overduelari_hesapla()
                results = session.query(BorrowingEntity).filter(BorrowingEntity.state.ilike("Overdue")).all()
                if results:
                    records = [record.to_dict() for record in results]
                    return json({"status": "success", "data": records})
                return json({"status": "error", "message": "No overdue borrowings found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def overduelari_hesapla():
        with SessionLocal() as session:
            try:
                #expected tarihi şimdiki tarihten geri olan ve state'i returned olmayan satırları bulup liste dönecek query
                #Bu listeyi dönüp her bir öğenin state'ini overdue yapacak for döngüsü
                results = session.query(BorrowingEntity).filter(BorrowingEntity.expected_date < datetime.now(),BorrowingEntity.state != "returned").all()
                for record in results:
                    record.state = "overdue"
                session.commit()
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_copy(request):
        with SessionLocal() as session:
            try:
                copy_id = int(request.args.get("copy"))
                results = session.query(BorrowingEntity).filter_by(copy=copy_id).first()
                if results:
                    result = results.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Borrowing not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_id(request):
        with SessionLocal() as session:
            try:
                id1 = int(request.args.get("id"))
                result = session.query(BorrowingEntity).filter_by(id=id1).first()
                if result:
                    result = result.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Borrowing not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_member(request):
        with SessionLocal() as session:
            try:
                member1 = int(request.args.get("member"))
                result = session.query(BorrowingEntity).filter_by(member=member1).first()
                if result:
                    result = result.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Borrowing not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_BorrowDate(request):
        with SessionLocal() as session:
            try:
                Borrow_date_str= request.args.get("borrow_date")
                borrow_date1 = datetime.strptime( Borrow_date_str, "%Y-%m-%d").date()
                results = session.query(BorrowingEntity).filter_by(borrow_date=borrow_date1).first()
                if results:
                    result = results.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Borrowing not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_return_Date(request):
        with SessionLocal() as session:
            try:
                return_date_str = request.args.get("return_date")
                return_date1 = datetime.strptime(return_date_str, "%Y-%m-%d").date()
                results = session.query(BorrowingEntity).filter_by(return_date=return_date1).first()
                if results:
                    result = results.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "Borrowing not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def get_borrowing_by_username(request):


        username1 = request.args.get("username")
        if not username1:  # Eğer username yoksa uyarı ver
            return json({"error": "Username parameter is required."})

        with SessionLocal() as session:
            try:
                # 1. Adım: Kullanıcıyı bul
                user = session.query(UserEntity).filter(
                UserEntity.username.ilike(f"%{username1}%")).first()

                if not user:  # Eğer kullanıcı yoksa hata döndür
                    return json({"error": f"No user found with the username '{username1}'."})

                # 2. Adım: Kullanıcının borrowing (ödünç alma) kaydını bul
                borrowing = session.query(BorrowingEntity).filter(
                    BorrowingEntity.member == user.id
                ).first()

                if not borrowing:  # Eğer borrowing kaydı yoksa hata döndür
                    return json({"error": f"No borrowing record found for user '{username1}'."})

                # 3. Adım: Borrowing kaydını JSON formatında dön
                return json({
                    "user": {
                        "id": user.id,
                        "username": user.username
                    },
                    "borrowing": borrowing.to_dict()  # Borrowing kaydını JSON formatına dönüştür
                })
            except Exception as e:
                return json({"error": f"An error occurred: {str(e)}"})
            finally:
                session.close()

    @staticmethod
    async def get_borrowing_by_name(request):

        name1 = request.args.get("name")
        if not name1:  # Eğer username yoksa uyarı ver
            return json({"error": "Username parameter is required."})

        with SessionLocal() as session:
            try:
                # 1. Adım: Kullanıcıyı bul
                user = session.query(UserEntity).filter(
                    UserEntity.name.ilike(f"%{name1}%")).first()

                if not user:  # Eğer kullanıcı yoksa hata döndür
                    return json({"error": f"No user found with the name '{name1}'."})

                # 2. Adım: Kullanıcının borrowing (ödünç alma) kaydını bul
                borrowing = session.query(BorrowingEntity).filter(
                    BorrowingEntity.member == user.id
                ).first()

                if not borrowing:  # Eğer borrowing kaydı yoksa hata döndür
                    return json({"error": f"No borrowing record found for user '{name1}'."})

                # 3. Adım: Borrowing kaydını JSON formatında dön
                return json({
                    "user": {
                        "id": user.id,
                        "username": user.username
                    },
                    "borrowing": borrowing.to_dict()  # Borrowing kaydını JSON formatına dönüştür
                })
            except Exception as e:
                return json({"error": f"An error occurred: {str(e)}"})
            finally:
                session.close()


    @staticmethod
    async def add_borrowing(request):
        with SessionLocal() as session:
            try:
                data = request.json
                copy_id = data.get("copy")
                existing_borrowing = session.query(BorrowingEntity).filter_by(copy=copy_id).first()
                if existing_borrowing:
                    return json({"status": "error", "message": "This copy already exists in borrowings"})
                new_borrowing = BorrowingEntity.from_dict(data)
                session.add(new_borrowing)
                session.commit()
                return text("status: success, message" "Borrowing added successfully")
            except Exception as e:
                session.rollback()
                return text("Borrowing cannot added", str(e))
            finally:
                session.close()

    @staticmethod
    async def update_borrowing(request):
        session = SessionLocal()
        try:
            data = request.json
            borrowing_id = data["id"]
            results = session.query(BorrowingEntity).filter_by(id=borrowing_id).first()
            if not results:
                return text("Borrowing not found")

            for key, value in data.items():
                if hasattr(results, key):
                    setattr(results, key, value)
            session.commit()
            return text("{)status: success, message: Borrowing record updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()

    @staticmethod
    async def delete_borrowing(request):
        session = SessionLocal()
        try:
            borrowing_id = int(request.args.get("id"))
            result = session.query(BorrowingEntity).filter_by(id=borrowing_id).first()
            if not result:
                return json({"status": "error", "message": "Borrowing not found"})
            session.delete(result)
            session.commit()
            return json({"status": "success", "message": "Borrowing deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()


