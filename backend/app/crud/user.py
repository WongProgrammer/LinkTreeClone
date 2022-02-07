from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import CreateUser
from app.models.user import User


def create_user(user: CreateUser, db: Session):
    try:
        new_user = User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't Create user."
        )
