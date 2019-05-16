from webapp.controller.common import header_checker, response, response_code
from webapp.models.orders import Order
import json
def create(request):
    neworedr=Order.objects.create()
    return response(response_code['OK'], {'order_id': neworedr.order_id})


def get_order(request):
    req=request.POST
    orderID=req.get('order_id')
    order=Order.objects.filter(order_id=orderID)
    return response(response_code['OK'], order)


def modify_order(request):
    req=request.POST
    order_id=req.get('order_id')
    customer_num =req.get('customer_num')
    #这个有问题，暂不清楚给的menu_list到底是什么格式
    menu_list = req.get('menu_list')
    status = req.get('status')
    worker_id = req.get('worker_id')
    order = Order.objects.filter(order_id=req.order_id)
    order.update(order_id=order_id,customer_num=customer_num,
                 menu_list=menu_list, status=status, worker_id=worker_id)
    return response(response_code['OK'])


def finish_order(request):
    req=request.POST
    orderID= req.get("order_id")
    totalPrice = 0
    order=Order.objects.filter(order_id=orderID)
    menulist_dict=json.load(s=order.menu_list)
    menu_list = menulist_dict['menu_list']
    return response(response_code['OK'], totalPrice)


def get_orders(request):
    orders=Order.objects.all()
    return_orders = list(orders)
    return response(response_code['OK'], return_orders)
