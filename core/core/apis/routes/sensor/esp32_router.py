from fastapi import APIRouter
from core.controllers.sensor.esp32_controller import SensorController
from core import logger

logging = logger(__name__)
esp32_router = APIRouter()


@esp32_router.post("/bhoomi/sensor/save_data")
async def save_sensor_data(
    water_temperature: float, tds_level: float, ph_level: float, water_level: int
):
    try:
        response = SensorController().update_sensor_data(
            water_level=water_level,
            water_temperature=water_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error
