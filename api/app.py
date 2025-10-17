# Main Web Application file 
# /api is the root folder for the web application
import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from site_generation.view import router as site_generation_router
from database.core import Base as DBBase, sync_engine

from config import Config
from logs import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init db
    DBBase.metadata.create_all(sync_engine)
    yield 
    

app = FastAPI(
    version=Config.API_VERSION, title=Config.APP_TITLE,
    lifespan=lifespan
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
