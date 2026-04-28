# scrapers/base.py

from abc import ABC, abstractmethod
from typing import List, Dict

class BaseScraper(ABC):
    def __init__(self, keywords: List[str], location: str):
        self.keywords = keywords
        self.location = location
        
    @abstractmethod
    def scrape(self)->List[Dict]:
        pass