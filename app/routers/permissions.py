import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas import PermissionBase, PermissionPublic
from app.dependencies.services import PermissionServiceDep


router = APIRouter(prefix="/permissions", tags=["Permissions"])


@router.get(path="/{permission_id}", response_model=PermissionPublic)
def get_permission(
    permission_id: int,
    service: PermissionServiceDep
):
    try:
        return service.get_permission(permission_id)
    except ValueError as ex:
        logging.error(f"Permission not found: {ex}")
        return JSONResponse(
            status_code=404,
            content={"message": "Permission not found"}
        )


@router.post(path="/", response_model=PermissionPublic)
def create_permission(
    permission: PermissionBase,
    service: PermissionServiceDep
):
    try:
        return service.create_permission(permission)
    except ValueError as ex:
        logging.error(f"Permission already exists: {ex}")
        return JSONResponse(
            status_code=400,
            content={"message": "Permission already exists"}
        )
    except Exception as ex:
        logging.error(f"Error creating permission: {ex}")
        return JSONResponse(
            status_code=500,
            content={"message": "Error creating permission"}
        )


@router.get(path="/", response_model=list[PermissionPublic])
def get_permissions(service: PermissionServiceDep):
    return service.get_all_permissions()


@router.put(path="/{permission_id}", response_model=PermissionPublic)
def update_permission(
    permission_id: int,
    permission: PermissionBase,
    service: PermissionServiceDep
):
    try:
        return service.update_permission(permission_id, permission)
    except ValueError as ex:
        logging.error(f"Permission not found: {ex}")
        return JSONResponse(
            status_code=404,
            content={"message": "Permission not fount"}
        )
    except Exception as ex:
        logging.error(f"Error updating permission: {ex}")
        return JSONResponse(
            status_code=500,
            content={"message": "Error updating permission"}
        )
