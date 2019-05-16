from django.urls import path
from webapp.controller import orders

urlpatterns = [
    path('create', orders.create, name='create'),

    path('get_order', orders.get_order, name='get_order'),
    path('modify_order', orders.modify_order, name='modify_order'),
    path('finish_order', orders.finish_order, name='finish_order'),

    path('get_orders', orders.get_orders, name='get_orders')
]