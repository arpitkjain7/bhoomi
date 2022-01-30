from core import session, logger
from core.orm_models.knn_historical_data import KNNHistoricalData

logging = logger(__name__)


class CRUDHistoricalData:
    def create(self, **kwargs):
        """[CRUD function to add a new User profile]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDSensorData create request")
            sensor_data = KNNHistoricalData(**kwargs)
            with session() as transaction_session:
                transaction_session.add(sensor_data)
                transaction_session.commit()
                transaction_session.refresh(sensor_data)
        except Exception as error:
            logging.error(f"Error in CRUDSensorData create function : {error}")
            raise error

    def read(self, position_id: str):
        """[CRUD function to read a User profile record]

        Args:
            user_name (str): [User name to filter the record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user record matching the criteria]
        """
        try:
            logging.info("CRUDSensorData read request")
            with session() as transaction_session:
                obj: KNNHistoricalData = (
                    transaction_session.query(KNNHistoricalData)
                    .filter(KNNHistoricalData.position_id == position_id)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read function : {error}")
            raise error

    def read_top_five(self):
        try:
            logging.info("CRUDSensorData read request")
            with session() as transaction_session:
                obj: KNNHistoricalData = (
                    transaction_session.query(KNNHistoricalData)
                    .order_by("created_at")
                    .limit(5)
                    .all()
                )
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read function : {error}")
            raise error

    def read_by_data(
        self,
        water_temp: float,
        air_temp: float,
        water_level: float,
        ph_level: float,
        tds_level: float,
    ):
        """[CRUD function to read a User profile record]

        Args:
            user_name (str): [User name to filter the record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user record matching the criteria]
        """
        try:
            logging.info("CRUDSensorData read request")
            with session() as transaction_session:
                obj: KNNHistoricalData = (
                    transaction_session.query(KNNHistoricalData)
                    .filter(KNNHistoricalData.air_temperature == air_temp)
                    .filter(KNNHistoricalData.water_temperature == water_temp)
                    .filter(KNNHistoricalData.water_level == water_level)
                    .filter(KNNHistoricalData.ph_level == ph_level)
                    .filter(KNNHistoricalData.tds_level == tds_level)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read_all User profile records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all user records]
        """
        try:
            logging.info("CRUDSensorData read_all request")
            with session() as transaction_session:
                obj: KNNHistoricalData = transaction_session.query(
                    KNNHistoricalData
                ).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read_all function : {error}")
            raise error

    def update(self, **kwargs):
        pass

    def delete(self, user_name: str):
        pass
