from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from core import Base


class RelayPositions(Base):
    __tablename__ = "relay_positions"
    __table_args__ = {"extend_existing": True}
    position_id = Column(Integer, primary_key=True, autoincrement=True)
    water_temp_relay = Column(Integer)
    tds_relay = Column(String)
    ph_relay = Column(String)
    temp_relay = Column(String)
    water_relay = Column(String)
