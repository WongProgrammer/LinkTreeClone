from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
import datetime as dt

from ..database.db import Base


class Domain(Base):
    __tablename__ = "domain"

    DomainID = Column(Integer, primary_key=True)
    Name = Column(String(100), unique=True, nullable=False)
    ImageUrl = Column(String(255), nullable=True)

    link = relationship(
        "Link", back_populates="domain", cascade="all, delete", passive_deletes=True
    )
