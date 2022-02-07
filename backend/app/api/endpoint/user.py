from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependency import get_db
from app.crud.user import create_user
from app.schemas.user import CreateUser, ReadUser

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create", response_model=ReadUser)
def create(user: CreateUser, db: Session = Depends(get_db)):
    return create_user(user, db)
