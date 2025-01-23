from sanic import Sanic, text
from sqlalchemy.dialects.postgresql import psycopg2
from backend.database import Base, engine
import book.BookBlueprint
import user.UserBlueprint
import image.ImageBlueprint
import copies.CopiesBlueprint
import auth.AuthBlueprint
import redis


# ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ
# Eğer oluşturulacak tablonun Blueprint'i import edilmemişse
# Entity dosyasının import edilmesi gerek, yoksa tablo oluşmaz.
# Eper Blueprint import edilmişse Entity import edilmemeli
# Eğer hem Entity, hem de Blueprint import edilirse tablo oluşturma fonksyonu
# Entity'yi iki kere gördüğünden hata veriyor.

#from book.BookEntity import BookEntity
r = redis.Redis(host='localhost', port=6380, db=0)

app = Sanic("LibraryManagementApp")

#Blueprintleri hem yukarda import etmek, hem de burdan belletmek gerekiyor
app.blueprint(book.BookBlueprint.bp)
app.blueprint(user.UserBlueprint.bp)
app.blueprint(copies.CopiesBlueprint.copies_blueprint )
app.blueprint(image.ImageBlueprint.bp)
app.blueprint(auth.AuthBlueprint.bp)

@app.listener("before_server_start")
async def setup_db(app, loop):
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

@app.get("/")
async def hello(request):
    print ("hello")
    return text("Hello, World!")


@app.get("/get_book/<book_id>")
async def get_book(request, book_id):
    cached_book = r.get(f"book:{book_id}")

    if cached_book:
        print("Cache'ten alınan kitap:")
        return text(f"Cache'ten alınan kitap: {cached_book.decode('utf-8')}")

    # Cache'te yoksa, veritabanına sorgu yaparak kitabı al
    conn = psycopg2.connect(
        host="localhost",
        database="PostgreSQL",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()

    if book:
        # Veritabanından alınan veriyi cache'e ekle
        r.set(f"book:{book_id}", str(book))
        print("Veritabanından alınan kitap:", book)
        return text(f"Veritabanından alınan kitap: {book}")

    return text("Kitap bulunamadı!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)











