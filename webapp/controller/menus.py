from webapp.controller.common import header_checker, response, response_code
from webapp.models import menus
from django.core import serializers


def create_item(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        new_item = menus.Menu.create_new_item()
        new_name = req.get('name')
        new_price = req.get('price')
        new_offset = req.get('offset')
        new_status = req.get('status')
        new_item.name = new_name
        new_item.price = new_price
        new_item.offset = new_offset
        if str(new_status) == 'true':
            new_item.status = True
        else:
            new_item.status = False
        new_item.save()
        return response(response_code['OK'])


def get_menus(request):
    if header_checker(request):
        items = menus.Menu.find_all_items()
        return response(response_code['OK'], serializers.serialize('json', items))
    return response(response_code['BAD_REQUEST'])


def get_menus_on_sell(request):
    if header_checker(request):
        items = menus.Menu.find_all_on_sell()
        return response(response_code['OK'], serializers.serialize('json', items))
    return response(response_code['BAD_REQUEST'])


def get_menu(request):
    if header_checker(request):
        req = request.GET
        item = menus.Menu.find_item(req.get('item_id'))
        return response(response_code['OK'], item)
    return response(response_code['BAD_REQUEST'])


def modify_menu_item(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        item_id = req.get('item_id')
        item = menus.Menu.find_item(item_id)
        if item:
            new_name = req.get('name')
            new_price = req.get('price')
            new_offset = req.get('offset')
            new_status = req.get('status')
            item.name = new_name
            item.price = new_price
            item.offset = new_offset
            if str(new_status) == 'true':
                item.status = True
            else:
                item.status = False
            item.save()
            return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def remove_menu_item(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        item_id = req.get('item_id')
        menus.Menu.remove_item(item_id)
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])
