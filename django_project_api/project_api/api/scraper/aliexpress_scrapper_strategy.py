from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from api.scraper.scraper_strategy import ScraperStrategy
from logger.logger import *

class AliexpressScraperStrategy(ScraperStrategy):

    def __str__(self):
        return "aliexpress"

    # @wrap(entering, exiting)
    def get_url(self, item):
        """Setting Aliexpress url"""
        splitted = item.split()
        if len(splitted) == 1:
            url = "https://es.aliexpress.com/af/" + item + ".html?d=y&origin=n&SearchText=" + \
                  item + "&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"
        elif len(splitted) > 1:
            link1 = ''
            link2 = ''
            minus = 1
            for i in splitted:
                if minus < len(splitted):
                    link1 = link1 + i + '-'
                    link2 = link2 + i + '+'
                else:
                    link1 = link1 + i
                    link2 = link2 + i
            minus += 1
            url = "https://es.aliexpress.com/af/" + link1 + ".html?d=y&origin=n&SearchText=" + \
                  link2 + "&catId=0&spm=a2g0o.productlist.1000002.0&initiative_id=SB_20220830102312"
        return url

    # @wrap(entering, exiting)
    def read_information(self, item):
        """Scrapping Aliexpress"""
        if item == '':
            raise ValueError(f"Invalid item: Please digit a valid item")
        else:
            url = self.get_url(item)
            option = Options()
            option.headless = True
            option.add_argument('--headless')
            # options.add_argument('window-size=1200x600')
            option.add_argument('--no-sandbox')
            option.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
            driver.get(url)
            return driver.page_source
