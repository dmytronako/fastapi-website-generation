import datetime
from fastapi import FastAPI
from src.config import Config

from src.logging import logger


app = FastAPI(
    version=Config.API_VERSION, title=Config.APP_TITLE
)


# Healthchecker endpoint
@app.get('/', response_model=str)
async def health() -> str:
    logger.debug('Request on healthcheck endpoint')
    curr_time = datetime.datetime.now()
    return f'TIME: {curr_time}'
