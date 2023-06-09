import unittest
from api.parser.parsers.amazon_parser import AmazonParser

class test_amazon_parser(unittest.TestCase):

	def test_amazon_list_is_not_empty(self):
		f =open('api/tests/response_amazon.txt')
		file = f.read()
		parser = AmazonParser()
		products = parser.parse(file)
		self.assertNotEqual(products, [])

	def test_amazon_dicts_is_not_empty(self):
		f =open('api/tests/response_amazon.txt')
		file = f.read()
		parser = AmazonParser()
		products = parser.parse(file)
		for product in products:
			self.assertNotEqual(product, {})

	def test_amazon_items_is_not_empty(self):
		f =open('api/tests/response_amazon.txt')
		file = f.read()
		parser = AmazonParser()
		products = parser.parse(file)
		for product in products:
			for key, value in product.items():
				self.assertNotEqual(value, None)




