#scrapers/indeed.py
from jobspy import scrape_jobs
from typing import List,Dict
from .base import BaseScraper

class IndeedScraper(BaseScraper):
    def scrape(self) -> List[Dict]:
        jobs = []
        for keyword in self.keywords:
            try:
                jobs.extend(self._scrape_keyword(keyword))
            except Exception as e:
                print(f"[Indeed] Error scraping '{keyword}': {e}")
        return jobs
    
    def _scrape_keyword(self, keyword:str) -> List[Dict]:
        jobs = []
        
        
        scraped_jobs = scrape_jobs(
            site_name=["indeed"],
            location=self.location,
            search_term=keyword,
            results_wanted=10,
            country_indeed="Philippines"
            )
        
        for index,row in scraped_jobs.iterrows():
            try:
                jobs.append({
                    "title": row["title"],
                    "company": row["company"],
                    "location": row["location"],
                    "url": row["job_url"],
                    "source": "Indeed",
                    "keyword": keyword,
                    "description": row.get("description"),
                    "posted_at": row.get("posted_at")
                })
            except Exception as e:
                print(f"[Indeed] Error processing job data: {e}")
                continue
        print(f"[Indeed] Scraped {len(jobs)} jobs for keyword '{keyword}'")
        return jobs
            