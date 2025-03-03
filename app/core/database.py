import os

from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.engine import create_engine


DB_URL = URL.create(
    drivername=os.getenv("DB_ENGINE"),
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)
DB_ENGINE = create_engine(DB_URL)


class Base(DeclarativeBase):
    pass


def create_session() -> Session:
    return Session(bind=DB_ENGINE, autoflush=False)
