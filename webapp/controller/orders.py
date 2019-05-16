from webapp.controller.common import header_checker, response, response_code
from webapp.models.orders import Order
from django.core import serializers
from webapp.models import logs
import json


def create(request):
    user = header_checker(request)
    if user:
        new_order = Order.objects.create()
        new_order.menu_list = '([],)'
        new_order.table_id = (-1,)
        new_order.status = "('ing',)"
        new_order.save()
        return response(response_code['OK'], new_order.order_id)
    return response(response_code['BAD_REQUEST'])


def get_order(request):
    req = request.GET
    order_id = req['order_id']
    order = Order.objects.get(order_id=int(order_id))
    return response(response_code['OK'], {'order_id': order.order_id, 'menu_list': eval(order.menu_list)[0],
                                          'table_id': eval(order.table_id)[0],
                                          'customer_num': order.customer_num,
                                          'start_time': order.start_time,
                                          'end_time': order.end_time,
                                          'status': order.status})


def modify_order(request):
    user = header_checker(request)
    if user:
        req = request.POST
        order_id = req.get('order_id')
        table_id = req.get('table_id')
        menu_list = req.get('menu_list')
        status = req.get('status')
        order = Order.find_item(order_id)
        order.table_id = table_id,
        order.status = status,
        order.person_id = user.person_id
        order.menu_list = menu_list,
        order.save()
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def finish_order(request):
    user = header_checker(request)
    if user:
        req = request.POST
        order_id = req.get('order_id')
        order = Order.find_item(order_id)
        status = req.get('status')
        order.status = status,
        order.save()
        logs.Log.create_order(order_id, user.worker_id, user.name)
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_orders(request):
    orders = Order.objects.filter(status="('ing',)")
    return_orders = list(orders)
    new_orders = []
    for order in return_orders:
        order.table_id = eval(order.table_id)[0]
        order.menu_list = eval(order.menu_list)[0]
        order.status = eval(order.status)[0]
        new_orders.append(order)
    print(new_orders)
    return response(response_code['OK'], serializers.serialize('json', new_orders))
