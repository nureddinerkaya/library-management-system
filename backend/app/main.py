from sanic import Sanic
from sanic.response import json
from backend.database import Base, engine
from book.BookService import *

app = Sanic("LibraryManagementApp")

## Create database tables
#@app.listener("before_server_start")
#async def setup_db(app, loop):
#    Base.metadata.create_all(bind=engine)

@app.route("/")
async def index(request):

    return json({"message": "Welcome to the Library Management System"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

new_book = create_book(
    name="1984",
    authors="George Orwell",
    category="Dystopian",
    date="1949-06-08",
    ISBN="123-4567890123",
    pages=328
)
print(f"Created book: {new_book.name}, Authors: {new_book.authors}")

print("adadaasdadsad")