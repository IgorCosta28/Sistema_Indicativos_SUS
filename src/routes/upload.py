from typing import List

from fastapi import APIRouter, Body, File, Form, UploadFile

from src.controllers.upload import upload,get_upload_all

upload_router = APIRouter(tags=["upload"])


@upload_router.post("/upload")
async def upload_file_indicative(input: str = Form(...), files: List[UploadFile] = File(...)):
    return await upload(input, files)

@upload_router.get('/upload')
async def get_files_indicative():
    return await get_upload_all()