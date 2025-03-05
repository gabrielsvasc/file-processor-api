from app.schemas import RoleCreate, RoleUpdate
from app.models import Role
from app.dependencies.repositories import RoleRepositoryDep


class RoleService:
    def __init__(self, repository: RoleRepositoryDep):
        self.repository = repository

    def create_role(self, role: RoleCreate) -> Role:
        if self.repository.get_role_by_name(role.name):
            raise ValueError(f"Role with name {role.name} already exists")

        return self.repository.create_role(role)

    def get_all_roles(self) -> list[Role]:
        return self.repository.get_all_roles()

    def get_role(self, role_id: int) -> Role:
        role = self.repository.get_role(role_id)

        if not role:
            raise ValueError(f"Role with id {role_id} not found")

        return role

    def update_role(self, role_id: int, role: RoleUpdate) -> Role:
        if not self.repository.get_role(role_id):
            raise ValueError(f"Role with id {role_id} not found")

        update_dict = role.model_dump(exclude_unset=True)
        return self.repository.update_role(role_id, update_dict)
