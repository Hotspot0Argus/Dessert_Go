from webapp.controller.common import header_checker, response, response_code
from webapp.models import menus
from webapp.models import persons


def create_item(request):
    new_item = menus.Menu.create_new_item()
    new_item.save()
    new_item_id = new_item.item_id
    return response(response_code['OK'], new_item_id)


def get_menus(request):
    items = menus.Menu.find_all_items()
    return response(response_code['OK'], items)


def modify_menu_item(request):
    person_id = header_checker(request)
    req = request.POST
    item_id = req.get('item_id')
    person = persons.Person.find_by_person_id(person_id)
    position = person.position
    if position > 1:
        item = menus.Menu.find_item(item_id)
        req = request.POST
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
    person_id = header_checker(request)
    req = request.POST
    item_id = req.get('item_id')
    person = persons.Person.find_by_person_id(person_id)
    position = person.position
    if position > 1:
        item = menus.Menu.remove_item(item_id)
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])