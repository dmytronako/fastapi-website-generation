from uuid import UUID
from fastapi import APIRouter
from site_generation.models import GenerateBody, GenerateResponse, LogsResponse


router = APIRouter()


@router.post('/generate', response_model=GenerateResponse)
async def generate(payload: GenerateBody) -> str:
    return 'generate'


@router.get('/site/{site_id}')
async def site(site_id: UUID) -> UUID:
    return site_id


@router.get('/logs', response_model=LogsResponse)
async def logs(offset: int) -> str:
    return 'logs'
