from app.core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped as Map,
    mapped_column,
)


class Permissions(Base):
    __tablename__ = "permissions"

    id: Map[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Map[str] = mapped_column(String(30), unique=True)
