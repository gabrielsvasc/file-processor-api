from app.dependencies.database import SessionDep
from app.models import Role
from app.schemas import (
    RoleCreate,
)


class RoleRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def create_role(self, role: RoleCreate) -> Role:
        role = Role(**role.model_dump())
        self.session.add(role)
        self.session.commit()
        self.session.refresh(role)

        return role

    def get_role(self, role_id: int) -> Role | None:
        return self.session.query(Role) \
            .filter(Role.id == role_id) \
            .first()

    def get_role_by_name(self, role_name: str) -> Role | None:
        return self.session.query(Role) \
            .filter(Role.name == role_name) \
            .first()

    def get_all_roles(self) -> list[Role]:
        return self.session.query(Role) \
            .all()
