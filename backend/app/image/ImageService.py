from sanic import json, text, response

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
                # Fetch the image by ID
                image_id = int(request.args.get("id"))
                image = session.query(ImageEntity).filter_by(id=image_id).first()
                if not image:
                    return response.json({"error": "Image not found"}, status=404)

                # Return the image data
                headers = {
                    "Content-Type": image.mime_type,
                    "Content-Disposition": f"inline; filename=image_{image.id}"
                }
                return response.raw(image.data, headers=headers)
            except Exception as e:
                return response.json({"error": str(e)}, status=500)
            finally:
                session.close()

    @staticmethod
    async def add_image(request):
        with SessionLocal() as session:
            try:
                new_image = ImageEntity.from_dict(request)
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
