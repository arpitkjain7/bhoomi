from sqlalchemy import Column, Integer, DateTime, Float
from core import Base


class SensorData(Base):
    __tablename__ = "sensor_data"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    water_temperature = Column(Float)
    air_temperature = Column(Float)
    tds_level = Column(Float)
    ph_level = Column(Float)
    water_level = Column(Integer)
    created_at = Column(DateTime)
