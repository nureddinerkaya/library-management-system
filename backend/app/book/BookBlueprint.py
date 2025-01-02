from sanic import Sanic, Blueprint
from sanic.response import json


# Define the Blueprint for Book entity
bp = Blueprint("BookBlueprint", url_prefix="/books")

# Example route to get all books
@bp.route("/", methods=["GET"])
async def get_books(request):
    return json({"message": "Retrieve all books"})

# Example route to add a new book
@bp.route("/", methods=["POST"])
async def add_book(request):
    return json({"message": "Add a new book"})