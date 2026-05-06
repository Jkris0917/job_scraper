#backend\routes\jobs.py

import math

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from backend.schemas import JobResponse,JobListResponse
from models import JobListing

router = APIRouter()

@router.get("/jobs",response_model=JobListResponse)
def get_jobs(db: Session = Depends(get_db), search: str= "", page: int=1,page_size: int = 10,):
    query = db.query(JobListing)
    if search:
        query = query.filter(JobListing.title.ilike(f"%{search}%"))
        
    total = query.count()
    jobs = query.offset((page - 1) * page_size).limit(page_size).all()
    last_page = max(1, math.ceil(total / page_size))
    
    return {"jobs": jobs, "last_page": last_page, "total": total}


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    if job := db.query(JobListing).filter(JobListing.id == job_id).first():
        return job
    else:
        raise HTTPException(status_code=404, detail="Job not found")
    