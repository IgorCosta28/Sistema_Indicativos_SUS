from fastapi import FastAPI
from .routes.index import index_router
app = FastAPI()

app.include_router(index_router)