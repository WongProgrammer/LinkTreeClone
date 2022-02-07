from fastapi import FastAPI

from app.models import user
from app.database.db import engine
from app.api.endpoint.user import router

app = FastAPI()

app.include_router(router)

user.Base.metadata.create_all(bind=engine)


@app.get("/")
def hello_world():
    return "Hello World"
