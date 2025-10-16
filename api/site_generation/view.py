from fastapi import APIRouter
from site_generation.models import GenerateBody, GenerateResponse


router = APIRouter()


@router.post('/generate', response_model=GenerateResponse)
async def generate(payload: GenerateBody) -> str:
    return 'generate'


@router.get('/site/{site_id}')
async def site(site_id: str) -> str:
    return site_id


@router.get('/logs')
async def logs() -> str:
    return 'logs'
