from core.crud.sensor_data_crud import CRUDSensorData
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
        tds_level: float,
        ph_level: float,
        water_level: int,
    ):
        try:
            logging.info("executing update_sensor_data function")
            crud_request = {
                "water_temperature": water_temperature,
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
