import imp
from core.utils.knn_prediction import get_nearest_neighbour
from core.crud.historical_data_crud import CRUDHistoricalData
from core import config, logger
from datetime import datetime

logging = logger(__name__)


class InferenceController:
    def __init__(self):
        pass
        self.CRUDHistoricalData = CRUDHistoricalData()
        # # self.temp_location = config.get("core_engine").get("temp_file_path")

    def get_prediction(
        self, water_temperature: float, tds_level: float, ph_level: float
    ):
        try:
            logging.info("executing update_sensor_data function")
            latest_five_items = self.CRUDHistoricalData.read_top_five()
            water_temperature_list = [water_temperature]
            ph_level_list = [ph_level]
            tds_level_list = [tds_level]
            data = {}
            for item in latest_five_items:
                water_temperature_list.append(item.get("water_temperature"))
                ph_level_list.append(item.get("ph_level"))
                tds_level_list.append(item.get("tds_level"))
            data.update(
                {
                    "water_temperature": water_temperature_list,
                    "tds_level": tds_level_list,
                    "ph_level": ph_level_list,
                }
            )
            prediction = get_nearest_neighbour(data=data)
            print(prediction)
            return {"predicted_category": str(prediction)}
        except Exception as error:
            logging.error(f"Error in update_sensor_data function: {error}")
            raise error
