# model.py
from sqlalchemy.orm import declarative_base
from datetime import datetime,timezone
from sqlalchemy import Column, Integer, String, DateTime,Text


Base = declarative_base()

class JobListing(Base):
    __tablename__ = 'job_listings'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255))
    location = Column(String(255))
    url = Column(String(255), unique=True, nullable=False)
    source = Column(String(255))
    keywords = Column(String(255))
    description = Column(Text)
    posted_at = Column(DateTime)
    scraped_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    