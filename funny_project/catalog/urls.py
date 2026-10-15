from django.urls import path
from .views import catalog_view, product_detail_view


app_name = 'catalog'

urlpatterns = [
    path('', catalog_view, name='catalog_list'),
    path('<slug:slug>/', product_detail_view, name='product_detail'),
]