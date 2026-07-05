from fastapi import APIRouter
from src.routes.upload import upload_router

index_router = APIRouter(prefix="/api")

index_router.include_router(upload_router)
