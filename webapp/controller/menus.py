from webapp.controller.common import header_checker, response, response_code
from webapp.models import menus
from webapp.models import persons


def create_item(request):
    user = header_checker(request)
    if user & user.position > 1:
        new_item = menus.Menu.create_new_item()
        new_item.save()
        new_item_id = new_item.item_id
        return response(response_code['OK'], new_item_id)


def get_menus(request):
    if header_checker(request):
        items = menus.Menu.find_all_items()
        return response(response_code['OK'], items)
    return response(response_code['BAD_REQUEST'])


def get_menu(request):
    if header_checker(request):
        req = request.GET
        item = menus.Menu.find_item(req.get('item_id'))
        return response(response_code['OK'], item)
    return response(response_code['BAD_REQUEST'])


def modify_menu_item(request):
    user = header_checker(request)
    if user & user.position > 1:
        req = request.POST
        item_id = req.get('item_id')
        item = menus.Menu.find_item(item_id)
        if item:
            new_name = req.get('new_name')
            new_price = req.get('new_price')
            new_offset = req.get('new_offset')
            new_status = req.get('new_status')
            item.name = new_name
            item.price = new_price
            item.offset = new_offset
            item.status = new_status
            item.save()
            return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def remove_menu_item(request):
    user = header_checker(request)
    if user & user.position > 1:
        req = request.POST
        item_id = req.get('item_id')
        menus.Menu.remove_item(item_id)
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])
