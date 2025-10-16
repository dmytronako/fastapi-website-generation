from fastapi import APIRouter


router = APIRouter()


@router.post('/')
async def generate() -> str:
    return 'generate'


@router.get('/site/{site_id}')
async def site(site_id: str) -> str:
    return site_id


@router.get('/logs')
async def logs() -> str:
    return 'logs'
