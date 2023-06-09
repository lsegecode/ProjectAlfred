from api.scraper.scraper_strategy import ScraperStrategy
import requests
from logger.logger import *

class AmazonScrapperStrategy(ScraperStrategy):
    def __init__(self):
        self.__template = 'https://www.amazon.com/s?k={}'
        self.__headers = {
        'authority': 'www.amazon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7,es-MX;q=0.6',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.com/s?k=teclado&crid=3MXBSWS1Z1PGW&sprefix=%2Caps%2C99&ref=nb_sb_ss_recent_1_0_recent',
        'rtt': '50',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-viewport-width': '1600',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'viewport-width': '1600',
        }
        self.url = None
        
    def __str__(self):
        return "amazon"

    @wrap(entering, exiting)
    def get_url(self, product_name):
        """Geting Amazon url"""
        product_name = product_name.replace(' ', '+')
        url = self.__template.format(product_name)
        return url

    @wrap(entering, exiting)
    def read_information(self, product_name):
        """Scraping Amazon"""
        self.url = self.get_url(product_name)
           
        if self.url:
            try:
                response = requests.get(self.url, headers=self.__headers)
                while str(product_name) not in (response.text):
                    
                    response = requests.get(self.url, headers=self.__headers)
            except Exception:
                
                raise ValueError('Invalid URL')

        else:
            
            raise TypeError('Missing search term')
        
        return response.text
