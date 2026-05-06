#backend/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    url: str
    source: Optional[str] = None
    keyword: Optional[str] = None
    description: Optional[str] = None
    posted_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class JobListResponse(BaseModel):
    jobs: list[JobResponse]
    total: int
    last_page: int
