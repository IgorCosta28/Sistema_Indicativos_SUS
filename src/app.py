from fastapi import FastAPI
from .routes.index import index_router
import os 

app = FastAPI()

src_path = os.path.join('src','upload')
os.makedirs(src_path,exist_ok=True)

app.include_router(index_router)