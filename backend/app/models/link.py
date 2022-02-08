from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
import datetime as dt

from ..database.db import Base


class Link(Base):
    __tablename__ = "link"

    LinkID = Column(Integer, primary_key=True)
    Link = Column(String(255), unique=True, nullable=False)
    CreateDate = Column(DateTime(timezone=True), default=dt.datetime.utcnow())
    UserID = Column(
        Integer, ForeignKey("user.UserID", ondelete="CASCADE"), nullable=False
    )
    DomainID = Column(Integer, ForeignKey("domain.DomainID"), nullable=True)

    owner = relationship("User", back_populates="links")
