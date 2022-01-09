from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from core import Base


class Actions(Base):
    __tablename__ = "actions"
    __table_args__ = {"extend_existing": True}
    row_id = Column(Integer, primary_key=True, autoincrement=True)
    knn_result = Column(String)
    created_at = Column(DateTime)
