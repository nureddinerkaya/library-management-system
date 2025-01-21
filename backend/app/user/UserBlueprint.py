from sanic import Sanic, Blueprint
from sanic.response import json

from backend.app.user.UserService import UserService

# Define the Blueprint for User entity
bp = Blueprint("UserBlueprint", url_prefix="/api/users")


@bp.route("/getAll", methods=["GET"])
async def get_users(request):
    # Example: GET /getAll
    return await UserService.get_all_users(request)


@bp.route("/getById", methods=["GET"])
async def get_user(request):
    # Example: GET /getById?id=123
    return await UserService.get_user_by_id(request)


@bp.route("/add", methods=["POST"])
async def add_user(request):
    # Example: POST /add
    # Request Body (JSON):
    # {
    #     "id" :
    #     "username":
    #     "name" :
    #     "password":
    #     "type":
    #     "phone":
    #     "signupDate":
    # }
    return await UserService.add_user(request)


@bp.route("/update", methods=["PUT"])
async def update_user(request):
    # Example: PUT /update
    # Request Body (JSON):
    # {
    #     "id":
    #     "güncellenecek sütün":
    # }
    return await UserService.update_user(request)


@bp.route("/delete", methods=["DELETE"])
async def delete_user(request):
    # Example: DELETE /delete?id=123
    return await UserService.delete_user(request)
