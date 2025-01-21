from sanic import json, text

from backend.app.image.ImageEntity import ImageEntity
from backend.database import SessionLocal


class ImageService:

    @staticmethod
    async def get_all_images(request):
        with SessionLocal() as session:
            results = session.query(ImageEntity).all()
            images = [image.to_dict() for image in results]
            return json(images)

    @staticmethod
    async def find_by_id(id):
        with SessionLocal() as session:
            image = session.query(ImageEntity).filter(ImageEntity.id == id).first()
            return image

    @staticmethod
    async def get_image_by_id(request):
        with SessionLocal() as session:
            try:
                image_id = int(request.args.get("id"))
                image = ImageService.find_by_id(id)
                if image:
                    result = image.to_dict()
                    return json({"status": "success", "data": result})
                return json({"status": "error", "message": "ImageEntity not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def add_image(request):
        with SessionLocal() as session:
            try:
                data = request.json #bu fonksiyon json payload'ını alıp python dict'ine dönüştürüyormuş
                new_image = ImageEntity.from_dict(data)
                session.add(new_image)
                session.commit()
                return text("status: success, message" "ImageEntity added successfully")
            except Exception as e:
                session.rollback()
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))
            finally:
                session.close()

    @staticmethod
    async def update_image(request):
        session = SessionLocal()
        try:
            data = request.json
            image_id = data["id"]
            image = session.query(ImageEntity).filter_by(id=image_id).first()
            if not image:
                return text("ImageEntity not found")

            for key, value in data.items():
                if hasattr(image, key):
                    setattr(image, key, value)
            session.commit()
            return text("{)status: success, message: ImageEntity updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()

    @staticmethod
    async def delete_image(request):
        session = SessionLocal()
        try:
            image_id = int(request.args.get("id"))
            image = session.query(ImageEntity).filter_by(id=image_id).first()
            if not image:
                return json({"status": "error", "message": "ImageEntity not found"})
            session.delete(image)
            session.commit()
            return json({"status": "success", "message": "ImageEntity deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()
