from datetime import datetime
from fastapi import APIRouter, Form
from core.controllers.sensor.esp32_controller import (
    SensorController,
    TargetPositionController,
    HistoricalDataController,
)
from core.apis.schemas.requests.sensor.esp32_requests import UpdateSensorData
from core import logger

logging = logger(__name__)
esp32_router = APIRouter()


@esp32_router.post("/bhoomi/sensor/save_data")
async def save_sensor_data(
    water_temperature: str = Form(...),
    air_temperature: str = Form(...),
    tds_level: str = Form(...),
    ph_level: str = Form(...),
    water_distance: str = Form(...),
):
    try:
        print(water_temperature)
        response = SensorController().update_sensor_data(
            water_distance=round(float(water_distance), 2),
            water_temperature=round(float(water_temperature), 2),
            air_temperature=round(float(air_temperature), 2),
            tds_level=round(float(tds_level), 2),
            ph_level=round(float(ph_level), 2),
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.get("/bhoomi/sensor/get_all")
async def get_sensor_data():
    try:
        return SensorController().get_sensor_data_100()
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error


@esp32_router.get("/bhoomi/sensor/get_latest")
async def get_latest_sensor_data():
    try:
        return SensorController().get_latest_sensor_data()
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


@esp32_router.post("/bhoomi/test")
async def create(
    water_temperature: str = Form(...),
    air_temperature: str = Form(...),
    tds_level: str = Form(...),
    ph_level: str = Form(...),
    water_distance: str = Form(...),
):
    try:
        return {"status": "success"}
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error
