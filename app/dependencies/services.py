from typing import Annotated
from fastapi import Depends
from app.services.roles import RoleService
from app.services.permissions import PermissionService

RoleServiceDep = Annotated[RoleService, Depends(RoleService)]
PermissionServiceDep = Annotated[PermissionService, Depends(PermissionService)]
