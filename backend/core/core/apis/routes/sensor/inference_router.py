from datetime import datetime
from fastapi import APIRouter
from core.controllers.sensor.inference_controller import InferenceController
from core import logger

logging = logger(__name__)
knn_inference_router = APIRouter()


@knn_inference_router.post("/bhoomi/prediction/get_position_id")
async def predict_position_id(
    water_temperature: float,
    tds_level: float,
    ph_level: float,
):
    try:
        response = InferenceController().get_prediction(
            water_temperature=water_temperature,
            tds_level=tds_level,
            ph_level=ph_level,
        )
        return response
    except Exception as error:
        logging.error(f"Error in /bhoomi/sensor/save_data endpoint: {error}")
        raise error
