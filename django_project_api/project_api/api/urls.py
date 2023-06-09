from django.urls import path
from .views import CRUDView
from api.rest_api.rest_api import RestApi

urlpatterns=[
    path('products/', CRUDView.as_view(), name="products_list"),
    path('products/<str:prod_name>', RestApi.get_products, name="products")
]
