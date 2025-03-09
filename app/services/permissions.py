from app.dependencies.repositories import PermissionRepositoryDep
from app.models import Permission
from app.schemas import PermissionCreate, PermissionUpdate


class PermissionService:
    def __init__(self, repository: PermissionRepositoryDep):
        self.repository = repository

    def get_permission(self, permission_id: int) -> Permission:
        permission = self.repository.get_permission(permission_id)

        if not permission:
            raise ValueError(f"Permission with id {permission_id} not found")

        return permission

    def get_all_permissions(self) -> list[Permission]:
        return self.repository.get_all_permissions()

    def create_permission(self, permission: PermissionCreate) -> Permission:
        if self.repository.get_permission_by_name(permission.name):
            raise ValueError(
                f"Permission with name {permission.name} already exists")

        return self.repository.create_permission(permission)

    def update_permission(
            self,
            permission_id: int,
            permission: PermissionUpdate
    ) -> Permission:
        if not self.repository.get_permission(permission_id):
            raise ValueError(f"Permission with id {permission_id} not found")

        update_dict = permission.model_dump(exclude_unset=True)
        return self.repository.update_permission(permission_id, update_dict)
