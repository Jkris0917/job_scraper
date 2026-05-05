#scrapers/indeed.py
from jobspy import scrape_jobs
from typing import List,Dict
from .base import BaseScraper

class IndeedScaper(BaseScraper):
    def scrape(self) -> List[Dict]:
        jobs = []
        for keyword in self.keywords:
            try:
                jobs.extend(self._scrape_keyword(keyword))
            except Exception as e:
                print(f"[Indeed] Error scraping '{keyword}': {e}")
        return jobs
    
    def _scrape_keyword(self, keyword:str) -> List[Dict]:
        scraped_jobs = scrape_jobs(site_name=["indeed"],location=self.location, search_term=keyword,results_wanted=10,country_indeed="Philippines")