from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import CreateUser, UserIn, UpdateUser
from app.models.user import User


def create_user(user: CreateUser, db: Session):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(user: UserIn, db: Session):
    return db.query(User).filter(User.Email == user.Email).first()


def get_user_by_id(id: int, db: Session):
    return db.query(User).filter(User.UserID == id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def update_user(id: int, request: UpdateUser, db: Session):
    user = db.query(User).filter(User.UserID == id)
    user.update({"FirstName": request.FirstName}, synchronize_session=False)
    db.commit()
    updated_user = user.first()
    db.refresh(updated_user)
    return updated_user


def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.UserID == id)
    user.delete()
    db.commit()
