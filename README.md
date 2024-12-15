## CENG 434 Web Tasarım ve Geliştirme dersi için Kütüphâne İdâre Nizâmesi projesi.

Eğer projeyi klonlayınca venv otomatikman oluşturulup requirements.txt'nin içindekiler kurulmuyorsa bunlar şöyle yapılmalı:

```
python -m venv venv

//Windows
venv\Scripts\activate

//macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Database

Şifre, user ve db "postgres" idir. Database'i kurmak için:

```
docker pull nureddin1/kutuphane-postgres:latest

docker run --name kutuphane-postgres -p 5432:5432 -d nureddin1/kutuphane-postgres:latest

```
