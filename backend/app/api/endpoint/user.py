from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.dependency import get_db
from ...schemas.user import ReadUser, CreateUser, UpdateUser
from ...crud.user import (
    create_user,
    get_user_by_email,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)


router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create", response_model=ReadUser, status_code=status.HTTP_201_CREATED)
def create(user: CreateUser, db: Session = Depends(get_db)):
    """
    Use this endpoint to create a user!
    """
    db_user = get_user_by_email(user, db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )
    return create_user(user, db)


@router.get("/", response_model=List[ReadUser])
def get_all(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/{id}", response_model=ReadUser)
def get_one(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this ID doesn't exist",
        )
    return user


@router.put("/{id}", response_model=ReadUser)
def update(id: int, request: UpdateUser, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this ID doesn't exist",
        )
    return update_user(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist.",
        )
    return delete_user(id, db)
