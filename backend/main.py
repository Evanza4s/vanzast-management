from fastapi import FastAPI
from internal.routes.router import router

app = FastAPI()

app.title = "Management System"
app.description = "API for MS"

app.include_router(router)

