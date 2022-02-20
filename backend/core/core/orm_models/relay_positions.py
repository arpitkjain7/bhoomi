from ast import Str
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from core import Base


class RelayPositions(Base):
    __tablename__ = "relay_positions"
    __table_args__ = {"extend_existing": True}
    position_id = Column(Integer, primary_key=True, autoincrement=True)
    water_heater_relay = Column(String)
    water_chiller_relay = Column(String)
    room_heater_relay = Column(String)
    room_chiller_relay = Column(String)
    nutrient_relay = Column(String)
    ph_up_relay = Column(String)
    ph_down_relay = Column(String)
    water_level_relay = Column(String)
