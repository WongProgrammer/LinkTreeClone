from fastapi import FastAPI

from app.models import link, user, domain
from app.database.db import engine, Base
from app.api.endpoint import user as user_endpoint

app = FastAPI()

app.include_router(user_endpoint.router)

Base.metadata.create_all(bind=engine)
