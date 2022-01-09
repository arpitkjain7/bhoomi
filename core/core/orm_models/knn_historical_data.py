from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from core import Base


class KNNHistoricalData(Base):
    __tablename__ = "knn_historical_data"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    water_temperature = Column(Integer)
    tds_level = Column(String)
    ph_level = Column(String)
    water_level = Column(String)
    target = Column(Integer, ForeignKey("target_positions.position_id"))
    status = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
