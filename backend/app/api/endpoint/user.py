from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.api.dependency import get_db
from ...schemas.user import ReadUser, CreateUser
from ...crud.user import create_user, get_user_by_email


router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create", response_model=ReadUser, status_code=status.HTTP_201_CREATED)
def create(user: CreateUser, db: Session = Depends(get_db)):
    """
    Use this endoint to create a user!
    """
    db_user = get_user_by_email(user.Email, db)
    if not db_user:
        raise HTTPException(
            status=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )
    return create_user(user, db)
