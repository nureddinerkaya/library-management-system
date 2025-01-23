# Base image olarak python 3.10 seçiyoruz
FROM python:3.11

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# Gereksinim dosyasını kopyala
COPY requirements.txt /app/

# Gereksinimleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# backend dizinini kopyala
COPY backend /app/backend

# PYTHONPATH ortam değişkenini /app olarak ayarlıyoruz
ENV PYTHONPATH=/app

# main.py dosyasını çalıştır
CMD ["python", "/app/backend/app/main.py"]
