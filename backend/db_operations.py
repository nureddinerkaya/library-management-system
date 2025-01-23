# backend/db_operations.py
import psycopg2

# PostgreSQL bağlantısı
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",  # Veritabanı adını buraya yazın
        user="postgres",           # PostgreSQL kullanıcı adınızı buraya yazın
        password="postgres"        # PostgreSQL şifrenizi buraya yazın
    )
    return conn

# Veritabanından veri alma
def get_book_from_db(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return book
