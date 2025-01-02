from sqlalchemy.orm import Session

from backend.app.book.BookEntity import BookEntity
from backend.database import SessionLocal


def create_book(name: str, authors: str, category: str, date: str, ISBN: str, pages: int):
    session: Session = SessionLocal()
    try:
        new_book = BookEntity(
            name=name,
            authors=authors,
            category=category,
            date=date,
            ISBN=ISBN,
            pages=pages,
        )
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book
    finally:
        session.close()


# Retrieve all books or a specific book by ID
def get_books():
    session: Session = SessionLocal()
    try:
        return session.query(BookEntity).all()
    finally:
        session.close()


def get_book_by_id(book_id: int):
    session: Session = SessionLocal()
    try:
        return session.query(BookEntity).filter(BookEntity.ID == book_id).first()
    finally:
        session.close()


# Update an existing book
def update_book(book_id: int, name: str = None, authors: str = None, category: str = None, date: str = None,
                ISBN: str = None, pages: int = None):
    session: Session = SessionLocal()
    try:
        book = session.query(BookEntity).filter(BookEntity.ID == book_id).first()
        if not book:
            return None
        if name:
            book.name = name
        if authors:
            book.authors = authors
        if category:
            book.category = category
        if date:
            book.date = date
        if ISBN:
            book.ISBN = ISBN
        if pages is not None:
            book.pages = pages
        session.commit()
        session.refresh(book)
        return book
    finally:
        session.close()


# Delete a book by ID
def delete_book(book_id: int):
    session: Session = SessionLocal()
    try:
        book = session.query(BookEntity).filter(BookEntity.ID == book_id).first()
        if not book:
            return None
        session.delete(book)
        session.commit()
        return book
    finally:
        session.close()
