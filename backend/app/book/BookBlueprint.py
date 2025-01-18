from sanic import Sanic, Blueprint
from sanic.response import json

from backend.app.book.BookService import BookService

# Define the Blueprint for Book entity
bp = Blueprint("BookBlueprint", url_prefix="/api/books")

#request.args.get("id")

@bp.route("/getAll", methods=["GET"])
async def get_books(request):
    # Example: GET /getAll
    return await BookService.get_all_books(request)


@bp.route("/getById", methods=["GET"])
async def get_book(request):
    # Example: GET /getById?id=123
    return await BookService.get_book_by_id(request)


#@bp.route("/getByISBN", methods=["GET"])
#async def get_book_by_isbn(request):
#    # Example: GET /getByISBN?isbn=9783161484100
#    return await BookService.get_book_by_isbn(request)
#
#
#@bp.route("/getByPublisher", methods=["GET"])
#async def get_book_by_publisher(request):
#    # Example: GET /getByPublisher?publisher=Penguin
#    return await BookService.get_books_by_publisher(request)
#
#
#@bp.route("/getByTitle", methods=["GET"])
#async def get_book_by_title(request):
#    # Example: GET /getByTitle?title=The+Great+Gatsby
#    return await BookService.get_books_by_title(request)
#
#
#@bp.route("/getByAuthors", methods=["GET"])
#async def get_book_by_author(request):
#    # Example: GET /getByAuthors?authors=F+Scott+Fitzgerald
#    return await BookService.get_books_by_author(request)
#
#
#@bp.route("/getByCategory", methods=["GET"])
#async def get_book_by_genre(request):
#    # Example: GET /getByCategory?category=Fiction
#    return await BookService.get_books_by_category(request)


@bp.route("/add", methods=["POST"])
async def add_book(request):
    # Example: POST /add
    # Request Body (JSON):
    # {
    #     "title": "New Book",
    #     "authors": "Jane Austen",
    #     "isbn": "0-061-96436-0",
    #     "publisher": "Publisher Name",
    #     "category": "Literature",
    #     "date":"1992-12-28",
    #     "pages":192
    # }
    return await BookService.add_book(request)


@bp.route("/update", methods=["PUT"])
async def update_book(request):
    # Example: PUT /update
    # Request Body (JSON):
    # {
    #     "id": 123,
    #     "title": "Updated Book Title",
    #     "author": "Updated Author Name"
    # }
    return await BookService.update_book(request)


@bp.route("/delete", methods=["DELETE"])
async def delete_book(request):
    # Example: DELETE /delete?id=123
    return await BookService.delete_book(request)
