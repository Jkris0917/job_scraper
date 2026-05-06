#scheduler.py

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
from scraper import run_scraper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_scrape():
    try:
        run_scraper()
    except Exception as e:
        logger.error(f"Scraper failed: {e}")
        
def start_scheduler():
    scheduler = BlockingScheduler()
    
    scheduler.add_job(
        func=safe_scrape,
        trigger=IntervalTrigger(minutes=2),
        id="job_scraper",
        replace_existing=True
    )
    
    try:
        logger.info("Scheduler Starts... running every 2 minutes")
        safe_scrape()
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Scheduler stopped.")
    except Exception as e:
        logger.error(f"Scheduler error: {e}")

if __name__ == "__main__":
    start_scheduler()