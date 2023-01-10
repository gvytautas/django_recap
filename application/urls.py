from django.urls import path
from .views import hello_world, index, add_stock, delete_stock, show_stock

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('', index, name='index'),
    path('show_stock/', show_stock, name='show_stock'),
    path('add_stock/', add_stock, name='add_stock'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock'),
]
