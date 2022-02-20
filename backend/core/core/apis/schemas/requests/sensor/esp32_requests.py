from typing import Optional
from pydantic import BaseModel


class UpdateSensorData(BaseModel):
    water_temperature: str
    air_temperature: str
    tds_level: str
    ph_level: str
    water_distance: str


class Test(BaseModel):
    water_temperature: str
