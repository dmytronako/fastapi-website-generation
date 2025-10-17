import os
from logs import logger


VALIDATION_FIELDS = [
    'DB_URL',
    'LLM_PROVIDER_URL',
    'LLM_MODEL',
    'LLM_API_KEY'
]


class Config:
    API_VERSION = '1.0'
    APP_TITLE = 'Site Generation Framework'
    DB_URL: str | None = os.getenv('DB_URL')
    LLM_PROVIDER_URL: str | None = os.getenv('LLM_PROVIDER_URL')
    LLM_MODEL: str | None = os.getenv('LLM_MODEL')
    LLM_API_KEY: str | None = os.getenv('LLM_API_KEY')


# Do config fields validation
for field in VALIDATION_FIELDS:
    v = getattr(Config, field)
    if v is None:
        logger.critical(
            f'''
            Critical error:\n Field {field} is none in the
            application environment variables. Shutting down the application...
            '''
        )
    
