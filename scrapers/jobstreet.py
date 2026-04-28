#scraper/jobstreet.py

import httpx
from bs4 import BeautifulSoup
from typing import List,Dict
from .base import BaseScraper

HEADERS = {
    "User-Agent" :(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

class JobStreetScraper(BaseScraper):
    BASE_URL = 'https://www.jobstreet.com.ph/jobs'
    
    def scrape(self)->List[Dict]:
        jobs = []
        for keyword in self.keywords:
            try:
                jobs.extend(self._scrape_keyword(keyword))
            except Exception as e:
                print(f"[JobStreet] Error scraping '{keyword}': {e}")
        return jobs
    
    def _scrape_keyword(self, keyword:str) -> List[Dict]:
        jobs = []
        params = {
            "q": keyword,
            "l": self.location,
        }
        
        with httpx.Client(headers=HEADERS, timeout=30) as client:
            response = client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.select("article[data-automation='normaljob']")
        
        for card in cards:
            try:
                title_el = card.select_one("a[data-automation='jobTitle']")
                company_el = card.select_one("a[data-automation='jobCompany']")
                location_el = card.select_one("a[data-automation='jobLocation']")
                
                title = title_el.get_text(strip=True) if title_el else "N/A"
                company = company_el.get_text(strip=True) if company_el else "N/A"
                location = location_el.get_text(strip=True) if location_el else "N/A"
                url = "https://www.jobstreet.com.ph" + title_el["href"] if title_el else None
                
                if not url:
                    continue
                
                jobs.append({
                    "title": title,
                    "company": company,
                    "location" : location,
                    "url": url,
                    "source": "JobStreet",
                    "keywords" : keyword,
                    "description" : None,
                    "posted_at" : None,
                })
            except Exception as e :
                print(f"[JobStreet] Error parsing card: {e}")
                continue
        print(f"[JobStreet] Found {len(jobs)} jobs for '{keyword}'")
        return jobs