from sanic import Sanic, Blueprint
from sanic.response import json

from backend.app.borrowing.BorrowingService import BorrowingService

# Define the Blueprint for Book entity
borrowing_blueprint = Blueprint("BorrowingBlueprint", url_prefix="/borrowing")

#request.args.get("id")

@borrowing_blueprint.route("/getAll", methods=["GET"])
async def get_all_borrowing(request):
    # Example: GET /getAll
    return await BorrowingService.get_all_borrowings(request)

@borrowing_blueprint.route("/getpendingborrowings", methods=["GET"])
async def get_pending_borrowing(request):
    # Example: GET /getAll
    return await BorrowingService.get_borrowing_whose_are_pending(request)


@borrowing_blueprint.route("/getactiveborrowings", methods=["GET"])
async def get_active_borrowing(request):
    # Example: GET /getAll
    return await BorrowingService.get_borrowing_whose_are_active(request)

@borrowing_blueprint.route("/getreturnedborrowings", methods=["GET"])
async def get_returned_borrowing(request):
    return await BorrowingService.get_borrowing_whose_are_returned(request)


@borrowing_blueprint.route("/getoverdueborrowings", methods=["GET"])
async def get_overdue_borrowing(request):
    return await BorrowingService.get_borrowing_whose_are_overdue(request)


@borrowing_blueprint.route("/getByCopy", methods=["GET"])
async def get_borrowing_by_copy(request):
    # Example: GET /getById?copy=1
    return await BorrowingService.get_borrowing_by_copy(request)


@borrowing_blueprint.route("/getById", methods=["GET"])
async def get_borrowings_by_id(request):
#    # Example: GET /getById?id=1
    return await BorrowingService.get_borrowing_by_id(request)
#
#
@borrowing_blueprint.route("/getByMember", methods=["GET"])
async def get_borrowings_by_member(request):
#    # Example: GET /getByMember?member=1
    return await BorrowingService.get_borrowing_by_member(request)
#
#
@borrowing_blueprint.route("/getByBorrowDate", methods=["GET"])
async def get_book_by_title(request):
#    # Example: GET /getByBorrowDate?borrow_date=2020-12-23
    return await BorrowingService.get_borrowing_by_BorrowDate(request)
#
#
@borrowing_blueprint.route("/getByReturnDate", methods=["GET"])
async def get_book_by_author(request):
#    # Example: GET /getByReturnDate?return_date=2023-11-26
    return await BorrowingService.get_borrowing_by_return_Date(request)
#
#
#@borrowing_blueprint.route("/getByCategory", methods=["GET"])
#async def get_book_by_genre(request):
#    # Example: GET /getByCategory?category=Fiction
#    return await BookService.get_books_by_category(request)


@borrowing_blueprint.route("/addborrow", methods=["POST"])
async def add_borrowings(request):
    # Example: POST /add
    # Request Body (JSON):
    # {
    #
    # }
    return await BorrowingService.add_borrowing(request)


@borrowing_blueprint.route("/updateborrow", methods=["PUT"])
async def update_borrowings(request):
    # Example: PUT /update
    # Request Body (JSON):
    # {
    #     "id": 123,
    #     "title": "Updated Book Title",
    #     "author": "Updated Author Name"
    # }
    return await BorrowingService.update_borrowing(request)


@borrowing_blueprint.route("/deleteborrowing", methods=["DELETE"])
async def delete_book(request):
    # Example:  /deleteborrowing?id=123
    return await BorrowingService.delete_borrowing(request)
