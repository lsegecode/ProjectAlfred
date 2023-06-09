import unittest
from api.parser.parsers.aliexpress_parser import AliexpressParser

class test_aliexpress_parser(unittest.TestCase):

	def test_aliexpress_list_is_not_empty(self):
		f = open('api/tests/ali.html', encoding="utf8")
		file = f.read()
		parser = AliexpressParser()
		products = parser.parse(file)
		self.assertNotEqual(products, [])

	def test_aliexpress_dicts_is_not_empty(self):
		f = open('api/tests/ali.html', encoding="utf8")
		file = f.read()
		parser = AliexpressParser()
		products = parser.parse(file)
		for product in products:
			self.assertNotEqual(product, {})

	def test_aliexpress_items_is_not_empty(self):
		f = open('api/tests/ali.html', encoding="utf8")
		file = f.read()
		parser = AliexpressParser()
		products = parser.parse(file)
		for product in products:
			for key, value in product.items():
				self.assertNotEqual(value, None)

