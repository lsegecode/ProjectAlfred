import requests
from api.scraper.scraper_strategy import ScraperStrategy
from logger.logger import *

class EbayScrapperStrategy(ScraperStrategy):
    def __init__(self) -> None:
        self.url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0"

    def __str__(self):
        return "ebay"

    @wrap(entering, exiting)
    def get_url(self, item):
        """Setting Ebay url"""
        item = item.split()
        item = "+".join(item)
        return self.url.format(item)
    
    @wrap(entering, exiting)
    def read_information(self,item):
        """Scrapping Ebay"""
        self.url = self.get_url(item)
        r = requests.get(self.url)
        try:
            r.status_code == 200
        except:
            print("Something go wrong")
        self.html = r.text
        return self.html
