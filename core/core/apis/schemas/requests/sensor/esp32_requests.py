from typing import Optional
from pydantic import BaseModel


class UpdateSensorData(BaseModel):
    water_te: str
    output_prefix: str
    text: str
    voice_id: str = "Joanna"
