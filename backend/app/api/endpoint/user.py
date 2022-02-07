from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependency import get_db
from app.crud.user import create_user
from app.schemas.user import CreateUser, ReadUser

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create", response_model=ReadUser, status_code=status.HTTP_201_CREATED)
def create(user: CreateUser, db: Session = Depends(get_db)):
    """
    Use this endoint to create a user!
    """
    return create_user(user, db)
