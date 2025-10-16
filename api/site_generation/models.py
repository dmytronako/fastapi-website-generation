from pydantic import BaseModel, Field
from sqlalchemy import Column
from uuid import UUID
import datetime


# Pydantic Models
class GenerateBody(BaseModel):
    topic: str = Field(..., min_length=1, max_length=150)  # forbid too long text requests
    pages_count: int = Field(..., ge=1, le=25)
    style: str = Field(..., min_length=1, max_length=150)
    max_tokens: int = Field(..., ge=1, le=100_000)
    
    
class SiteMetaData(BaseModel):
    id: UUID  # Id of the site
    title: str
    
    
class RequestMetaData(BaseModel):
    topic: str
    style: str
    max_tokens: int
    pages_count: int
    id: UUID  # Request ID
    created_at: datetime.datetime  # when created


# Gonna returns titles and site ids (metadata) for later access
class GenerateResponse(BaseModel):
    request: RequestMetaData
    sites: list[SiteMetaData]


class LogsResponse(BaseModel):
    offset: int = Field(..., ge=1)  # How many last responses will be returned 
    requests: list[RequestMetaData]
    
    
# SQLAlchemy Models
