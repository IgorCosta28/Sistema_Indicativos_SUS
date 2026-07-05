from fastapi import FastAPI
from .routes.index import index_router
import os 

app = FastAPI()

os.makedirs('upload',exist_ok=True)

app.include_router(index_router)