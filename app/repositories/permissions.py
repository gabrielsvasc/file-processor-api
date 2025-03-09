from app.dependencies.database import SessionDep
from app.models import Permission
from app.schemas import PermissionCreate


class PermissionRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def create_permission(self, permission: PermissionCreate) -> Permission:
        permission = Permission(**permission.model_dump())

        self.session.add(permission)
        self.session.commit()
        self.session.refresh(permission)

        return permission

    def get_permission(self, permission_id: int) -> Permission | None:
        return self.session.query(Permission) \
            .filter(Permission.id == permission_id) \
            .first()

    def get_permission_by_name(
            self,
            permission_name: str
    ) -> Permission | None:
        return self.session.query(Permission) \
            .filter(Permission.name == permission_name) \
            .first()

    def get_all_permissions(self) -> list[Permission]:
        return self.session.query(Permission) \
            .all()

    def update_permission(
            self,
            permission_id: int,
            update_dict: dict
    ) -> Permission:
        rows_affected = self.session.query(Permission) \
            .filter(Permission.id == permission_id) \
            .update(update_dict)

        if rows_affected > 1:
            self.session.rollback()
            raise Exception("More than one permission updated")

        self.session.commit()
        return self.get_permission(permission_id)
