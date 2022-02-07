from time import timezone
from sqlalchemy import Column, String, Integer, DateTime
import datetime as dt

from app.database.db import Base


class Link(Base):
    __tablename__ = "link"

    LinkID = Column(Integer, primary_key=True)
    Link = Column(String(255), unique=True, nullable=False)
    CreateDate = Column(
        DateTime(timezone=True), default=dt.datetime.now(timezone="UTC")
    )
