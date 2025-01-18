from sanic import Sanic
from sanic.response import json
from backend.database import Base, engine
import book.BookBlueprint
from copies.Copies import *

# ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ ÖNEMLİ
# Eğer oluşturulacak tablonun Blueprint'i import edilmemişse
# Entity dosyasının import edilmesi gerek, yoksa tablo oluşmaz.
# Eğer hem Entity, hem de Blueprint import edilirse tablo oluşturma fonksyonu
# Entity'yi iki kere gördüğünden hata veriyo.

#from book.BookEntity import BookEntity

app = Sanic("LibraryManagementApp")

#Blueprintleri hem yukarda import etmek
app.blueprint(book.BookBlueprint.bp)

@app.listener("before_server_start")
async def setup_db(app, loop):
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

@app.route("/")
async def index(request):
    return json({"message": "Welcome to the Library Management System"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)