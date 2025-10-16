# Main Web Application file 
# /api is the root folder for the web application
import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from site_generation.view import router as site_generation_router

from config import Config
from logging import logger


app = FastAPI(
    version=Config.API_VERSION, title=Config.APP_TITLE
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Healthchecker endpoint
@app.get('/', response_model=str)
async def health() -> str:
    logger.debug('Request on healthcheck endpoint')
    curr_time = datetime.datetime.now()
    return f'TIME: {curr_time}'

# include router without prefix
app.include_router(site_generation_router, prefix='')
