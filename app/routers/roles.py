import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas import RolePublic, RoleBase
from app.dependencies.services import RoleServiceDep


router = APIRouter(prefix="/roles")


@router.get(path="/{role_id}", response_model=RolePublic)
def get_role(role_id: int, service: RoleServiceDep):
    try:
        return service.get_role(role_id)
    except ValueError as ex:
        logging.error(f"Role not found: {ex}")
        return JSONResponse(
            status_code=404,
            content={"message": "Role not found"}
        )


@router.post(path="/", response_model=RolePublic)
def create_role(role: RoleBase, service: RoleServiceDep):
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


@router.put(path="/{role_id}", response_model=RolePublic)
def update_role(role_id: int, role: RoleBase, service: RoleServiceDep):
    try:
        return service.update_role(role_id, role)
    except ValueError as ex:
        logging.error(f"Role not found: {ex}")
        return JSONResponse(
            status_code=404,
            content={"message": "Role not fount"}
        )
    except Exception as ex:
        logging.error(f"Error updating role: {ex}")
        return JSONResponse(
            status_code=500,
            content={"message": "Error updating role"}
        )
