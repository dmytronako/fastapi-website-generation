from pydantic import BaseModel, Field
from sqlalchemy import Column
from uuid import UUID
import datetime


class GenerateBody(BaseModel):
    topic: str = Field(..., min_length=1, max_length=150)  # forbid too long text requests
    pages_count: int = Field(..., ge=1, le=25)
    style: str = Field(..., min_length=1, max_length=150)
    max_tokens: int = Field(..., ge=1, le=100_000)
    
    
class SiteMetaData:
    id: UUID  # Id of the site
    title: str


# Gonna returns titles and site ids (metadata) for later access
class GenerateResponse(BaseModel):
    topic: str
    style: str
    max_tokens: int
    pages_count: int
    id: UUID  # Request ID
    sites: list[SiteMetaData]
    time: datetime.datetime
