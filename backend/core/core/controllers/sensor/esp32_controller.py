import imp
from core.crud.sensor_data_crud import CRUDSensorData
from core.crud.position_data_crud import CRUDPositionData
from core.crud.historical_data_crud import CRUDHistoricalData
from core import config, logger
from datetime import datetime

logging = logger(__name__)


class SensorController:
    def __init__(self):
        self.CRUDSensorData = CRUDSensorData()
        # self.temp_location = config.get("core_engine").get("temp_file_path")

    def update_sensor_data(
        self,
        water_temperature: float,
        air_temperature: float,
        tds_level: float,
        ph_level: float,
        water_level: int,
    ):
        try:
            logging.info("executing update_sensor_data function")
            crud_request = {
                "water_temperature": water_temperature,
                "air_temperature": air_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
                "water_level": water_level,
                "created_at": datetime.now(),
            }
            response = self.CRUDSensorData.create(**crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error

    def get_sensor_data(self):
        try:
            logging.info("executing update_sensor_data function")
            response = self.CRUDSensorData.read_all()
            return response
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
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
            response = self.CRUDPositionData.create(**crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error

    def get_position_id(self, water_temp, tds_level, ph_level):
        try:
            logging.info("executing update_sensor_data function")
            return self.CRUDPositionData.read_by_data(
                water_temp=water_temp,
                tds_level=tds_level,
                ph_level=ph_level,
            )
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
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
            logging.info("executing update_sensor_data function")
            crud_request = {
                "water_temperature": water_temperature,
                "air_temperature": air_temperature,
                "tds_level": tds_level,
                "ph_level": ph_level,
                "water_level": water_level,
                "target": target,
                "created_at": recorded_date,
            }
            print(crud_request)
            response = self.CRUDHistoricalData.create(**crud_request)
            return response
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error

    # def get_position_id(self, water_temp, air_temp, tds_level, ph_level, water_level):
    #     try:
    #         logging.info("executing update_sensor_data function")
    #         return self.CRUDPositionData.read_by_data(
    #             water_level=water_level,
    #             water_temp=water_temp,
    #             air_temp=air_temp,
    #             tds_level=tds_level,
    #             ph_level=ph_level,
    #         )
    #     except Exception as error:
    #         logging.error(f"Error in update_sensor_data function: {error}")
    #         raise error
