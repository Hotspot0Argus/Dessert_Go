from django.urls import path
from webapp.controller import orders

urlpatterns = [
    path('create', orders.create, name='create'),

    path('get_order/<int:order_id>', orders.get_order, name='get_order'),
    path('modify_order/<int:order_id>', orders.modify_order, name='modify_order'),
    path('finish_order/<int:order_id>', orders.finish_order, name='finish_order'),

    path('get_orders', orders.get_orders, name='get_orders')
]