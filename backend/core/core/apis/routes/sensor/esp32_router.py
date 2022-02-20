from datetime import datetime
from fastapi import APIRouter
from core.controllers.sensor.esp32_controller import (
    SensorController,
    TargetPositionController,
    HistoricalDataController,
)
from core import logger

logging = logger(__name__)
esp32_router = APIRouter()


@esp32_router.post("/bhoomi/sensor/save_data")
async def save_sensor_data(
    water_temperature: float,
    air_temperature: float,
    tds_level: float,
    ph_level: float,
    water_distance: float,
):
    try:
        response = SensorController().update_sensor_data(
            water_distance=water_distance,
            water_temperature=water_temperature,
            air_temperature=air_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.post("/bhoomi/sensor/get")
async def get_sensor_data():
    try:
        return SensorController().get_sensor_data()
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.post("/bhoomi/target/save_data")
async def save_target_data(
    water_temperature: str,
    tds_level: str,
    ph_level: str,
):
    try:
        response = TargetPositionController().update_sensor_data(
            water_temperature=water_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.post("/bhoomi/target/get_position")
async def create(
    water_temperature: str,
    tds_level: str,
    ph_level: str,
):
    try:
        response = TargetPositionController().get_position_id(
            water_temp=water_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.post("/bhoomi/knn/historical_data")
async def create(
    water_temperature: str,
    air_temperature: str,
    tds_level: str,
    ph_level: str,
    water_level: str,
    target: int,
    recorded_date: datetime,
):
    try:
        response = HistoricalDataController().create_record(
            water_level=water_level,
            water_temperature=water_temperature,
            air_temperature=air_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
            target=target,
            recorded_date=recorded_date,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error
