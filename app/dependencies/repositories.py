from typing import Annotated
from fastapi import Depends
from app.repositories.roles import RoleRepository

RoleRepositoryDep = Annotated[RoleRepository, Depends(RoleRepository)]
