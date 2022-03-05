import imp
from core.crud.sensor_data_crud import CRUDSensorData
from core.crud.position_data_crud import CRUDPositionData
from core.crud.historical_data_crud import CRUDHistoricalData
from core.controllers.sensor.inference_controller import InferenceController
from core.utils.common import getWaterLevel
from core import config, logger
from datetime import datetime

logging = logger(__name__)


class SensorController:
    def __init__(self):
        self.CRUDSensorData = CRUDSensorData()
        self.CRUDHistoricalData = CRUDHistoricalData()
        self.CRUDPositionData = CRUDPositionData()
        # self.temp_location = config.get("core_engine").get("temp_file_path")

    def update_sensor_data(
        self,
        water_temperature: float,
        air_temperature: float,
        tds_level: float,
        ph_level: float,
        water_distance: int,
    ):
        try:
            logging.info("executing update_sensor_data function")
            water_level = getWaterLevel(water_distance=water_distance)
            logging.info("Creating sensor data record")
            crud_request = {
                "water_temperature": water_temperature,
                "air_temperature": air_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
                "water_level": water_level,
                "created_at": datetime.now(),
            }
            logging.debug(f"{crud_request=}")
            self.CRUDSensorData.create(**crud_request)
            logging.info("Getting prediction")
            response = InferenceController().get_prediction(
                water_temperature=water_temperature,
                tds_level=tds_level,
                ph_level=ph_level,
            )
            logging.info("Creating historical data record")
            crud_historical_request = {
                "water_temperature": water_temperature,
                "air_temperature": air_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
                "water_level": water_level,
                "target": response.get("predicted_category"),
                "created_at": datetime.now(),
            }
            self.CRUDHistoricalData.create(**crud_historical_request)
            logging.info("Getting relay positions")
            relay_positions = self.CRUDPositionData.read(
                position_id=response.get("predicted_category")
            )
            return relay_positions
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error

    def get_sensor_data(self):
        try:
            logging.info("executing get_sensor_data function")
            return self.CRUDSensorData.read_all()
        except Exception as error:
            logging.error(f"Error in get_sensor_data function: {error}")
            raise error

    def get_sensor_data_100(self):
        try:
            logging.info("executing get_sensor_data function")
            return self.CRUDSensorData.read_latest_100_records()
        except Exception as error:
            logging.error(f"Error in get_sensor_data function: {error}")
            raise error

    def get_latest_sensor_data(self):
        try:
            logging.info("executing get_latest_sensor_data function")
            response = self.CRUDSensorData.read_latest()
            return response
        except Exception as error:
            logging.error(f"Error in get_latest_sensor_data function: {error}")
            raise error


class TargetPositionController:
    def __init__(self):
        self.CRUDPositionData = CRUDPositionData()
        # self.temp_location = config.get("core_engine").get("temp_file_path")

    def update_sensor_data(
        self,
        water_temperature: float,
        tds_level: float,
        ph_level: float,
    ):
        try:
            logging.info("executing update_sensor_data function")
            crud_request = {
                "water_temperature": water_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
            }
            logging.debug(f"{crud_request=}")
            response = self.CRUDPositionData.create(**crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error

    def get_position_id(self, water_temp, tds_level, ph_level):
        try:
            logging.info("executing get_position_id function")
            return self.CRUDPositionData.read_by_data(
                water_temp=water_temp,
                tds_level=tds_level,
                ph_level=ph_level,
            )
        except Exception as error:
            logging.error(f"Error in get_position_id function: {error}")
            raise error


class HistoricalDataController:
    def __init__(self):
        self.CRUDHistoricalData = CRUDHistoricalData()
        # self.temp_location = config.get("core_engine").get("temp_file_path")

    def create_record(
        self,
        water_temperature: float,
        air_temperature: float,
        tds_level: float,
        ph_level: float,
        water_level: int,
        target: int,
        recorded_date: datetime,
    ):
        try:
            logging.info("executing create_historical_record function")
            crud_request = {
                "water_temperature": water_temperature,
                "air_temperature": air_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
                "water_level": water_level,
                "target": target,
                "created_at": recorded_date,
            }
            logging.debug(f"{crud_request=}")
            response = self.CRUDHistoricalData.create(**crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in create_historical_record function: {error}")
            raise error
