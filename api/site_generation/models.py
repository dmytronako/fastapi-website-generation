from __future__ import annotations
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, ForeignKey, Text, DATETIME, String, VARCHAR, UUID as SQLAlchemyUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
import datetime
from database.core import Base


# Pydantic Models
# Convention is to use Model suffix for pydantic models
class GenerateBodyModel(BaseModel):
    topic: str = Field(..., min_length=1, max_length=150)  # forbid too long text requests
    pages_count: int = Field(..., ge=1, le=25)
    style: str = Field(..., min_length=1, max_length=150)
    max_tokens: int = Field(..., ge=1, le=100_000)
    
    
class SiteMetadataModel(BaseModel):
    id: UUID  # Id of the site
    title: str
    
    
class RequestMetadataModel(BaseModel):
    topic: str
    style: str
    max_tokens: int
    pages_count: int
    id: UUID  # Request ID
    created_at: datetime.datetime  # when created


# Gonna returns titles and site ids (metadata) for later access
class GenerateResponseModel(BaseModel):
    request: RequestMetadataModel
    sites: list[SiteMetadataModel]
    

class LogsResponseModel(BaseModel):
    offset: int = Field(..., ge=1)  # How many last responses will be returned 
    requests: list[RequestMetadataModel]
    
    
# SQLAlchemy Models
# Having two tables
# 1. Generate for general requests handling
# 2. Sites - consist generated sites with corresponded statuses
class Generate(Base):
    __tablename__ = 'generate'
    
    id: Mapped[UUID] = mapped_column(SQLAlchemyUUID, primary_key=True)
    topic: Mapped[str] = mapped_column(VARCHAR(1024), nullable=False)
    style: Mapped[str] = mapped_column(VARCHAR(1024), nullable=False)
    max_tokens: Mapped[int] = mapped_column(Integer, nullable=False)
    pages_count: Mapped[int] = mapped_column(Integer, nullable=False)
    sites: Mapped[list[Site]] = relationship('Site', back_populates='generate', uselist=True)
    
    
class Site(Base):
    __tablename__ = 'site'
    
    id: Mapped[UUID] = mapped_column(SQLAlchemyUUID, primary_key=True)
    status: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    html: Mapped[str] = mapped_column(Text, nullable=True)
    generate_id: Mapped[UUID] = mapped_column(SQLAlchemyUUID, ForeignKey('generate.id'))
    generate: Mapped[Generate] = relationship('Generate', back_populates='sites')
