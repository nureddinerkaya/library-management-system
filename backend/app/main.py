from sanic import Sanic
from sanic.response import json
from backend.database import Base, engine
from book.BookEntity import BookEntity
import book.BookBlueprint
from copies.Copies import *

app = Sanic("LibraryManagementApp")

app.blueprint(book.BookBlueprint.bp)

# Create database tables
@app.listener("before_server_start")
async def setup_db(app, loop):
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

@app.route("/")
async def index(request):
    return json({"message": "Welcome to the Library Management System"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)