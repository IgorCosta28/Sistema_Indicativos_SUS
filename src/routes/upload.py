from fastapi import APIRouter, Body

from src.controllers.upload import upload

upload_router = APIRouter(tags=["upload"])


@upload_router.post("/upload")
async def upload_file_indicative(input=Body(...)):
    return await upload(input)
