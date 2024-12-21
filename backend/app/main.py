from sanic import Sanic
from sanic.response import json
from backend.database import Base, engine

#Oluşturduğumuz entity classların database'de de oluşturulması için onları buraya import etmemiz icab ediyor.
from book.BookEntity import Book

app = Sanic("LibraryManagementApp")

# Create database tables
@app.listener("before_server_start")
async def setup_db(app, loop):
    Base.metadata.create_all(bind=engine)

@app.route("/")
async def index(request):
    return json({"message": "Welcome to the Library Management System"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)