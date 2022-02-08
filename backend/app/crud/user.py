from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import CreateUser, UserIn
from app.models.user import User


def create_user(user: CreateUser, db: Session):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(request: UserIn, db:Session):
    return db.query(User).filter(User.Email==request.Email)
    
