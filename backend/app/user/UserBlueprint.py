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
    #     "title": "New User",
    #     "authors": "Jane Austen",
    #     "isbn": "0-061-96436-0",
    #     "publisher": "Publisher Name",
    #     "category": "Literature",
    #     "date":"1992-12-28",1.	Introduction
    #     "pages":192
    # }
    return await UserService.add_user(request)


@bp.route("/update", methods=["PUT"])
async def update_user(request):
    # Example: PUT /update
    # Request Body (JSON):
    # {
    #     "id": 123,
    #     "title": "Updated User Title",
    #     "author": "Updated Author Name"
    # }
    return await UserService.update_user(request)


@bp.route("/delete", methods=["DELETE"])
async def delete_user(request):
    # Example: DELETE /delete?id=123
    return await UserService.delete_user(request)
