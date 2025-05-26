from fastapi import FastAPI
from internal.routes.router import router

app = FastAPI()

app.include_router(router)