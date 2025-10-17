from uuid import UUID
from fastapi import APIRouter
from site_generation.models import (
    GenerateBodyModel, GenerateResponseModel, LogsResponseModel
)
from database.core import AsyncDBSession
from site_generation.service import create_generate_request
from site_generation.ai.titles import generate_titles

router = APIRouter()


@router.post('/generate', response_model=GenerateResponseModel)
async def generate(
    payload: GenerateBodyModel, async_db_session: AsyncDBSession
) -> list[str]:
    # Put request into DB
    await create_generate_request(payload, async_db_session=async_db_session)
    titles = await generate_titles(
        payload.topic, payload.style, payload.pages_count, retry=3
    )
    # Here some logic for generation of sites itself must be presented
    # so far, just return titles
    return titles


@router.get('/site/{site_id}')
async def site(site_id: UUID, async_db_session: AsyncDBSession) -> UUID:
    return site_id


@router.get('/logs', response_model=LogsResponseModel)
async def logs(offset: int, async_db_session: AsyncDBSession) -> str:
    return 'logs'
