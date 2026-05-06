# scraper.py
from dotenv import load_dotenv
import os
from scrapers.indeed import IndeedScraper
from scrapers.google import GoogleScraper
from database import SessionLocal
from models import JobListing
from notifier import run_notify
load_dotenv()

def get_keywords():
    raw = os.getenv("KEYWORDS", "")
    keywords = [k.strip() for k in raw.split(",") if k.strip()]
    if not keywords:
        print("Warning: No keywords provided. Check your .env file.")
    return keywords
    
def get_location():
    location = os.getenv("LOCATION", "").strip()
    return location
        
def save_jobs(jobs: list):

    session = SessionLocal()
    new_jobs = []
    try:
        for job in jobs:
            existing_job = session.query(JobListing).filter_by(url=job["url"]).first()
            keywords_value = job.get("keywords") or job.get("keyword")
            if not existing_job:
                new_job = JobListing(
                    title=job["title"],
                    company=job["company"],
                    location=job["location"],
                    url=job["url"],
                    source=job["source"],
                    keyword=keywords_value,
                    description=job.get("description"),
                    posted_at=job.get("posted_at"),
                )
                session.add(new_job)
                new_jobs.append(job)
        session.commit()
    finally:
        session.close()
    return new_jobs

def run_scraper():
    keywords = get_keywords()
    location = get_location()
    all_jobs = []

    indeed_scraper = IndeedScraper(keywords, location)
    all_jobs.extend(indeed_scraper.scrape())

    google_scraper = GoogleScraper(keywords, location)
    all_jobs.extend(google_scraper.scrape())

    print(f"Total jobs found: {len(all_jobs)}")

    new_jobs = save_jobs(all_jobs)
    print(f"New jobs saved: {len(new_jobs)}")
    
    if new_jobs:
        run_notify(new_jobs)

if __name__ == "__main__":
    run_scraper()