from app.core.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped as Map,
    mapped_column,
)


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id: Map[int] = mapped_column(
        ForeignKey("roles.id"),
        primary_key=True
    )
    permission_id: Map[int] = mapped_column(
        ForeignKey("permissions.id"),
        primary_key=True
    )
