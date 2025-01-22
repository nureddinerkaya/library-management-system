from sanic import Sanic, text
from backend.database import Base, engine
import user.UserBlueprint
import copies.CopiesBlueprint
import auth.AuthBlueprint

# Sanic Uygulamanızı başlatıyorsunuz
app = Sanic("LibraryManagementApp")

# Blueprintlerinizi uygulamaya ekliyorsunuz
app.blueprint(user.UserBlueprint.bp)
app.blueprint(copies.CopiesBlueprint.copies_blueprint)
app.blueprint(auth.AuthBlueprint.bp)

# Uygulama başlatılmadan önce veritabanı tablolarını oluşturun
@app.listener("before_server_start")
async def setup_db(app, loop):
    # Veritabanındaki tüm tabloları oluşturuyoruz
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

# Basit bir test rotası
@app.get("/")
async def hello(request):
    return text("Hello, World!")

# Uygulamanın ana çalıştırma bloğu
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)












