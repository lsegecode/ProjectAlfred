from .db_manager.db_manager import DbManager
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

products_mesa_mock = [
	{"name":"mesa marron","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mesa azul","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mesa amarilla","price":3,"image_url":"sdsds","url":"sadasd"}
	]

products_mouse_mock = [
	{"name":"mouse marron","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mouse azul","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mouse amarilla","price":3,"image_url":"sdsds","url":"sadasd"}
	]

def parser(item):
	if item == 'mouse':
		product = products_mouse_mock
	else:
		product = products_mesa_mock
	return product


class CRUDView(View):

	def get(self, request, search_term):
		db_manager = DbManager()
		search = db_manager.find_term(search_term)
		if search:
			search = db_manager.term_up_today(search)
			if search:
				data = db_manager.find_products(search)
			else:
				db_manager.delete_search(search_term)
				db_manager.create(parser(search_term),search_term)
		else:
			db_manager.create(parser(search_term),search_term)
			data = parser(search_term)
		return JsonResponse(data, safe = False)
		