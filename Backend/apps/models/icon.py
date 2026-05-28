from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from .base import Base


class Icon(Base):
    __tablename__ = "icons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    svg_path = Column(Text, nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
