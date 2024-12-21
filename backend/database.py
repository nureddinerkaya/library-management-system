# database.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:5432/postgres")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
