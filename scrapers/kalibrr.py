# scrapers/kalibrr.py

import httpx
from typing import List,Dict
from .base import BaseScraper

class KalibrrScraper(BaseScraper):
    BASE_URL = "https://www.kalibrr.com/api/jobs_board/jobs"
    
    def scrape(self) -> List[Dict]:
        jobs = []
        for keyword in self.keywords:
            try:
                jobs.extend(self._scraper_keyword(keyword))
            except Exception as e:
                print(f"[Kalibrr] Error scraping '{keyword}': {e}")
        return jobs
    
    def _scraper_keyword(self,keyword=str) -> List[Dict]:
        jobs = []
        params = {
            "limit": 10,
            "offset" : 0,
            "keyword" : keyword,
            "location" : self.location
        }
        
        with httpx.Client(timeout=30) as client:
            response = client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
        for job in data.get("jobs",[]):
            try:
                jobs.append({
                    "title" : job.get("name","N/A"),
                    "company" : job.get("company", {}).get("name", "N/A"),
                    "location": job.get("location", [{}])[0].get("name", self.location),
                    "url":         f"https://www.kalibrr.com/c/{job.get('company', {}).get('slug')}/jobs/{job.get('id')}",
                    "source":      "Kalibrr",
                    "keyword":     keyword,
                    "description": job.get("description", None),
                    "posted_at":   None,
                })
            except Exception as e:
                print(f"[Kalibrr] Error parsing job: {e}")
                continue
        print(f"[Kalibrr] Found {len(jobs)} jobs for '{keyword}'")
        return jobs
        