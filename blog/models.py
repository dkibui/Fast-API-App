from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=True)
