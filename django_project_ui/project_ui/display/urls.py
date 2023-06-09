from django.urls import path
from . import views

urlpatterns = [
     path('search',views.Receiver.get_products, name = 'products'),
     path('home', views.index, name='home')
]
