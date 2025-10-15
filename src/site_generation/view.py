from fastapi import APIRouter


router = APIRouter(tags=['Generate Site'])


@router.post('/')
async def generate() -> str:
    return 'generate'


@router.get('/site/{site_id}')
async def site() -> str:
    return 'site id'


@router.get('/logs')
async def logs() -> str:
    return 'logs'
