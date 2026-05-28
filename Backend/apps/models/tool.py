from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Tool(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    icon_id = Column(Integer, ForeignKey("icons.id"), nullable=False)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)

    project = relationship("Project", backref="tools")
    icon = relationship("Icon", backref="tools")
