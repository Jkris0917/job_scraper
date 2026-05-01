# scraper.py
from dotenv import load_dotenv
import os
from scrapers import jobstreet,kalibrr
from database import SessionLocal
from models import JobListing
# TODO: import your two scrapers from scrapers/
# TODO: import SessionLocal from database.py
# TODO: import JobListing from models.py

load_dotenv()

def get_keywords():
    # TODO: read KEYWORDS from .env
    # hint: os.getenv("KEYWORDS", "")
    # hint: split by comma → return a list
    
    keywords = os.getenv("KEYWORDS", "")
    

def get_location():
    # TODO: read LOCATION from .env
    location = os.getenv("LOCATION","")
    
def save_jobs(jobs: list):
    # TODO: open a DB session
    # TODO: loop through jobs
    # TODO: check if url already exists in DB (avoid duplicates)
    # hint: session.query(JobListing).filter_by(url=job["url"]).first()
    # TODO: if not exists → create JobListing object and add to session
    # TODO: commit and close session
    # TODO: return count of NEW jobs saved
    session = SessionLocal()

def run_scraper():
    keywords = get_keywords()
    location = get_location()
    all_jobs = []

    # TODO: create JobStreetScraper and call .scrape() → extend all_jobs
    # TODO: create KalibrrScraper and call .scrape() → extend all_jobs

    print(f"Total jobs found: {len(all_jobs)}")

    # TODO: call save_jobs(all_jobs)
    # TODO: print how many new jobs were saved
    pass

if __name__ == "__main__":
    run_scraper()