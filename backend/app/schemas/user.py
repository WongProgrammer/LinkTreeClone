import datetime as dt
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    UserID: int
    FirstName: str
    LastName: str


class CreateUser(BaseModel):
    FirstName: str
    LastName: str
    Email: EmailStr


class ReadUser(BaseModel):
    UserID: int
    FirstName: str
    LastName: str
    Email: EmailStr
    CreateDate: dt.datetime

    class Config:
        orm_mode = True


class DeleteUser(BaseModel):
    Email: EmailStr
