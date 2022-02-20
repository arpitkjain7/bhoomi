from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from core import Base


class TargetPositions(Base):
    __tablename__ = "target_positions"
    __table_args__ = {"extend_existing": True}
    position_id = Column(Integer, primary_key=True, autoincrement=True)
    water_temperature = Column(String)
    tds_level = Column(String)
    ph_level = Column(String)
