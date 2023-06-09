import unittest

from api.scraper.scraper import Scraper


class TestScraper(unittest.TestCase):

    def test_scraper_instance(self):
        scraper = Scraper()
        self.assertTrue(isinstance(scraper, Scraper))

    def test_scrap_page(self):
        from api.scraper.ebay_scrapper_strategy import EbayScrapperStrategy
        scraper = Scraper()
        result = scraper.scrap_page(EbayScrapperStrategy(), "shirt")
        k = list(result.keys())
        self.assertIsInstance(result, dict)
        self.assertIn("ebay", result)

    def test_scrap(self):
        product = "shirt"
        scraper = Scraper()
        result = scraper.scrap(product)
        self.assertIsInstance(result, list)
        self.assertIn("amazon", result[0])
        self.assertIn("ebay", result[1])
        self.assertIn("aliexpress", result[2])

    def test_exception_product_empty(self):
        with self.assertRaises(ValueError):
            product = ""
            scraper = Scraper()
            result = scraper.scrap(product)

