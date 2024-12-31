from sanic import Sanic, text
from backend.database import Base, engine
from book.BookEntity import BookEntity
import book.BookBlueprint

app = Sanic("LibraryManagementApp")

app.blueprint(book.BookBlueprint.bp)

# Create database tables
@app.listener("before_server_start")
async def setup_db(app, loop):
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

@app.get("/")
async def hello(request):
    print ("hello")
    return text("Hello, World!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)











