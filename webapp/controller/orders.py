from webapp.controller.common import header_checker, response, response_code
from webapp.models.orders import Order
from django.core import serializers
import json


def create(request):
    new_order = Order.objects.create()
    return response(response_code['OK'], new_order.order_id)


def get_order(request):
    req = request.POST
    order_id = req.get('order_id')
    order = Order.objects.filter(order_id=order_id)
    return response(response_code['OK'], order)


def modify_order(request):
    req = request.POST
    order_id = req.get('order_id')
    customer_num = req.get('customer_num')
    menu_list = req.get('menu_list')
    status = req.get('status')
    worker_id = req.get('worker_id')
    order = Order.objects.filter(order_id=req.order_id)
    order.update(order_id=order_id, customer_num=customer_num,
                 menu_list=menu_list, status=status, worker_id=worker_id)
    return response(response_code['OK'])


def finish_order(request):
    req = request.POST
    order_id = req.get("order_id")
    total_price = 0
    order = Order.objects.filter(order_id=order_id)
    menu_list_dict = json.load(s=order.menu_list)
    menu_list = menu_list_dict['menu_list']
    return response(response_code['OK'], total_price)


def get_orders(request):
    orders = Order.objects.filter(status='ing')
    return_orders = list(orders)
    return response(response_code['OK'], serializers.serialize('json', return_orders))
