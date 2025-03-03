import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas import RoleCreate, RolePublic
from app.dependencies.services import RoleServiceDep


router = APIRouter(prefix="/roles")


# TODO: implement auth in the router
@router.post(path="/", response_model=RolePublic)
def create_role(role: RoleCreate, service: RoleServiceDep):
    try:
        return service.create_role(role)
    except ValueError as ex:
        logging.error(f"Role already exists: {ex}")
        return JSONResponse(
            status_code=400,
            content={"message": "Role already exists"}
        )
    except Exception as ex:
        logging.error(f"Error creating role: {ex}")
        return JSONResponse(
            status_code=500,
            content={"message": "Error creating role"}
        )


@router.get(path="/", response_model=list[RolePublic])
def get_roles(service: RoleServiceDep):
    return service.get_all_roles()
