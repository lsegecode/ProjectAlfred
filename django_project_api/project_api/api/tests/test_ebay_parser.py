import unittest, requests
from api.parser.parsers.ebay_parser import EbayParser

class test_ebay_parser(unittest.TestCase):

	def test_ebay_list_is_not_empty(self):
		URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camisa+para+hombre&_sacat=0"
		r= requests.get(URL)
		file = r.text
		parser = EbayParser()
		products = parser.parse(file)
		self.assertNotEqual(products, [])

	def test_ebay_dicts_is_not_empty(self):
		URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camisa+para+hombre&_sacat=0"
		r= requests.get(URL)
		file = r.text
		parser = EbayParser()
		products = parser.parse(file)
		for product in products:
			self.assertNotEqual(product, {})

	def test_ebay_items_is_not_empty(self):
		URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=camisa+para+hombre&_sacat=0"
		r= requests.get(URL)
		file = r.text
		parser = EbayParser()
		products = parser.parse(file)
		for product in products:
			for key, value in product.items():
				self.assertNotEqual(value, None)

