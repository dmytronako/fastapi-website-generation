import os
from logs import logger


class Config:
    API_VERSION = '1.0'
    APP_TITLE = 'Site Generation Framework'
    DB_URL: str | None = os.getenv('DB_URL')


# Do validation
if Config.DB_URL is None:
    logger.critical('URL to DB is not provided. Application collapses...')
    # logic to shut down app
