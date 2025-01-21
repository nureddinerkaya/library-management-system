from sanic import Sanic, Blueprint
from sanic.response import json

from backend.app.image.ImageService import ImageService

# Define the Blueprint for Image entity
bp = Blueprint("ImageBlueprint", url_prefix="/api/images")


@bp.route("/getAll", methods=["GET"])
async def get_images(request):
    # Example: GET /getAll
    return await ImageService.get_all_images(request)

@bp.route("/getById", methods=["GET"])
async def get_image(request):
    # Example: GET /getById?id=123
    return await ImageService.get_image_by_id(request)

@bp.route("/add", methods=["POST"])
async def add_image(request):
    return await ImageService.add_image(request)

@bp.route("/update", methods=["PUT"])
async def update_image(request):
    return await ImageService.update_image(request)

@bp.route("/delete", methods=["DELETE"])
async def delete_image(request):
    return await ImageService.delete_image(request)
