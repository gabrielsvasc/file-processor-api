from app.core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped as Map,
    mapped_column,
)


class Role(Base):
    __tablename__ = "roles"

    id: Map[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Map[str] = mapped_column(String(20), unique=True)
    permissions: Map[list[str]] = mapped_column(String(30), nullable=False)
