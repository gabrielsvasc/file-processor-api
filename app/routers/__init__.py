from app.routers.roles import router as roles_router
from app.routers.permissions import router as permissions_router

__all__ = [
    "roles_router",
    "permissions_router",
]
