from sqlalchemy import Column, Integer, String, DateTime
import datetime as dt


from app.database.db import Base


class User(Base):
    __tablename__ = "user"

    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Email = Column(String(150), unique=True, nullable=False)
    CreateDate = Column(DateTime(timezone=True), default=dt.datetime.now())
