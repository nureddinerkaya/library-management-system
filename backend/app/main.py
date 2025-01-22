from sanic import Sanic, text
from backend.database import Base, engine
import book.BookBlueprint
import user.UserBlueprint
import  copies.CopiesBlueprint
import borrowing.BorrowingBlueprint
# ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ
# Eğer oluşturulacak tablonun Blueprint'i import edilmemişse
# Entity dosyasının import edilmesi gerek, yoksa tablo oluşmaz.
# Eper Blueprint import edilmişse Entity import edilmemeli
# Eğer hem Entity, hem de Blueprint import edilirse tablo oluşturma fonksyonu
# Entity'yi iki kere gördüğünden hata veriyor.

#from book.BookEntity import BookEntity

app = Sanic("LibraryManagementApp")

#Blueprintleri hem yukarda import etmek, hem de burdan belletmek gerekiyor
app.blueprint(book.BookBlueprint.bp)
app.blueprint(user.UserBlueprint.bp)
app.blueprint(copies.CopiesBlueprint.copies_blueprint )
app.blueprint(borrowing.BorrowingBlueprint.borrowing_blueprint)

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











