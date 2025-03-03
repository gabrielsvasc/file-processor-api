from typing import Annotated
from fastapi import Depends
from app.services.roles import RoleService

RoleServiceDep = Annotated[RoleService, Depends(RoleService)]
