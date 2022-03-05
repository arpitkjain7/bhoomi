from core import session, logger
from core.orm_models.sensor_data import SensorData
from sqlalchemy import desc

logging = logger(__name__)


class CRUDSensorData:
    def create(self, **kwargs):
        """[CRUD function to add a new User profile]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            logging.info("CRUDSensorData create request")
            sensor_data = SensorData(**kwargs)
            with session() as transaction_session:
                transaction_session.add(sensor_data)
                transaction_session.commit()
                transaction_session.refresh(sensor_data)
        except Exception as error:
            logging.error(f"Error in CRUDSensorData create function : {error}")
            raise error

    def read(self, row_id: str):
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
                obj: SensorData = (
                    transaction_session.query(SensorData)
                    .filter(SensorData.row_id == row_id)
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
                obj: SensorData = transaction_session.query(SensorData).all()
                logging.info(obj)
            if obj is not None:
                logging.info([row.__dict__ for row in obj])
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read_all function : {error}")
            raise error

    def read_latest_100_records(self):
        """[CRUD function to read_all User profile records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all user records]
        """
        try:
            logging.info("CRUDSensorData read_all request")
            with session() as transaction_session:
                obj: SensorData = (
                    transaction_session.query(SensorData)
                    .order_by(desc(SensorData.created_at))
                    .limit(100)
                    .all()
                )
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read_all function : {error}")
            raise error

    def read_latest(self):
        """[CRUD function to read_latest User profile records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all user records]
        """
        try:
            logging.info("CRUDSensorData read_latest request")
            with session() as transaction_session:
                obj: SensorData = (
                    transaction_session.query(SensorData)
                    .order_by(desc(SensorData.created_at))
                    .limit(2)
                    .all()
                )
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            logging.error(f"Error in CRUDSensorData read_latest function : {error}")
            raise error

    def update(self, **kwargs):
        pass

    def delete(self, user_name: str):
        pass
