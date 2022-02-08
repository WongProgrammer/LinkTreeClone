from fastapi import FastAPI

from app.models import link, user
from app.database.db import engine, Base
from app.api.endpoint import user

app = FastAPI()

app.include_router(user.router)

Base.metadata.create_all(bind=engine)
