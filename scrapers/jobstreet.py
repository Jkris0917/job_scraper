# scrapers/jobstreet.py
import httpx
from typing import List, Dict
from .base import BaseScraper

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://ph.jobstreet.com/",
}

class JobStreetScraper(BaseScraper):
    BASE_URL = "https://ph.jobstreet.com/api/chalice-search/v4/search"

    def scrape(self) -> List[Dict]:
        jobs = []
        for keyword in self.keywords:
            try:
                jobs.extend(self._scrape_keyword(keyword))
            except Exception as e:
                print(f"[JobStreet] Error scraping '{keyword}': {e}")
        return jobs

    def _scrape_keyword(self, keyword: str) -> List[Dict]:
        jobs = []
        params = {
            "siteKey":    "PH-Main",
            "where":      self.location,
            "what":       keyword,
            "pageSize":   10,
            "page":       1,
        }

        with httpx.Client(headers=HEADERS, timeout=30, follow_redirects=True) as client:
            response = client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

        for job in data.get("data", []):
            try:
                jobs.append({
                    "title":       job.get("title", "N/A"),
                    "company":     job.get("advertiser", {}).get("description", "N/A"),
                    "location":    job.get("location", self.location),
                    "url":         "https://ph.jobstreet.com/job/" + str(job.get("id")),
                    "source":      "JobStreet",
                    "keyword":     keyword,
                    "description": job.get("teaser", None),
                    "posted_at":   None,
                })
            except Exception as e:
                print(f"[JobStreet] Error parsing job: {e}")
                continue

        print(f"[JobStreet] Found {len(jobs)} jobs for '{keyword}'")
        return jobs