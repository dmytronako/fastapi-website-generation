from sqlalchemy.ext.asyncio.session import AsyncSession
from site_generation.models import SiteMetadataModel, Site, Generate, GenerateBodyModel
from logs import logger


async def create_generate_request(
    generate_body_model: GenerateBodyModel,
    *,
    async_db_session: AsyncSession
):
    """
        Put generate request in DB.
        
        TIME and UUID created automatically on DB side
    """
    generate_body_model = generate_body_model.model_dump()
    generate = Generate(**generate_body_model)
    await async_db_session.add(generate)
    await async_db_session.commit()
    await async_db_session.refresh(generate)
    logger.debug(f'Generate request {generate.id} put into DB')


async read_generate_requests(
    async_db_session: AsyncSession
) -> list[]:
    