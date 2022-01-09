# Database Manager
from core.database.database_manager import DatabaseManager
from commons.logger import logger

database_manager = DatabaseManager.sharedInstance()
Base = database_manager.Base
from core.database.context_manager import session

# Create Tables
from core.orm_models import *

print("db created")
Base.metadata.create_all(bind=database_manager.engine)
from commons.load_config import load_configuration

config = load_configuration()
