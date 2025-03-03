from fastapi import FastAPI
from app.routers import (
    roles_router,
)

app = FastAPI(
    title="FileProcessor",
    summary="API for control big data file upload, processing and lifecycle.",
)
app.include_router(roles_router)
