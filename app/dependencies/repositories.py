from typing import Annotated
from fastapi import Depends
from app.repositories.roles import RoleRepository
from app.repositories.permissions import PermissionRepository

RoleRepositoryDep = Annotated[RoleRepository, Depends(RoleRepository)]
PermissionRepositoryDep = Annotated[
    PermissionRepository,
    Depends(PermissionRepository)
]
