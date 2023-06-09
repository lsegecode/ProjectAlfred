from api.scraper.scraper_strategy import ScraperStrategy
from api.scraper.amazon_scrapper_strategy import AmazonScrapperStrategy
from api.scraper.ebay_scrapper_strategy import EbayScrapperStrategy
from api.scraper.aliexpress_scrapper_strategy import AliexpressScraperStrategy
from logger.logger import *

class Scraper:

    def __init__(self):
        self.strategies = [AmazonScrapperStrategy(), EbayScrapperStrategy(), AliexpressScraperStrategy()]
    
    @wrap(entering, exiting)
    def scrap_page(self, strategy: ScraperStrategy, product) -> {str: str}:
        """Using scrappers"""
        result = strategy.read_information(product)
    
        return {str(strategy): result}

    @wrap(entering, exiting)
    def scrap(self, product) -> [{str: str}]:
        """Getting scrappers"""
        if product != "":
            lst = []
            for s in self.strategies:
                lst.append(self.scrap_page(s, product))
            return lst
        else:
            raise ValueError("There is not a product")
