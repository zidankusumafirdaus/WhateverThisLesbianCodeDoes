from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class SourcingLocation(Base):
    __tablename__ = "sourcing_locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    store_name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    distance_km = Column(Numeric(8, 2), nullable=False)
    provides = Column(String(255), nullable=True)
    google_maps_url = Column(String(255), nullable=True)

    project = relationship("Project", backref="sourcing_locations")
