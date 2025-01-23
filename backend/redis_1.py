import redis
import json

# Redis'e bağlan
r = redis.Redis(host='localhost', port=6380, db=0)

# Cache'lenmiş kitap verisi ekleme fonksiyonu
def cache_book(book_id, book_data):
    # Veriyi JSON formatında cache'e ekliyoruz
    r.setex(f'book:{book_id}', 900, json.dumps(book_data))  # 15 dakika boyunca saklanacak

# Cache'ten kitap verisi alma fonksiyonu
def get_book_from_cache(book_id):
    cached_data = r.get(f'book:{book_id}')
    if cached_data:
        return json.loads(cached_data)
    else:
        return None  # Cache'te bulunmazsa None döner

# Cache'ten kitap verisi kontrol etme ve veritabanına düşme (örneğin burada manuel veritabanı yerine print ile simülasyon yapıyoruz)
def fetch_book(book_id):
    book = get_book_from_cache(book_id)
    if book:
        print("Cache'ten kitap alındı:", book)
    else:
        print("Cache'te bulunamadı, veritabanından alınıyor...")
        # Veritabanından almak gerekse burada işlemi yapabilirsin
        book = {
            'id': book_id,
            'title': 'Example Book Title',
            'author': 'Author Name',
            'year': 2022
        }
        # Kitap verisini cache'e ekle
        cache_book(book_id, book)
        print("Kitap veritabanından alındı ve cache'e eklendi:", book)

# Örnek kitap verisini cache'e ekleyip almak
fetch_book(1)
fetch_book(1)  # Bu sefer cache'ten alınacak

