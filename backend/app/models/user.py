from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime as dt


from ..database.db import Base


class User(Base):
    __tablename__ = "user"

    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(100), nullable=False)
    LastName = Column(String(100), nullable=False)
    Email = Column(String(150), unique=True, nullable=False)
    CreateDate = Column(DateTime(timezone=True), default=dt.datetime.utcnow())

    links = relationship(
        "Link", back_populates="owner", cascade="all, delete", passive_deletes=True
    )
