from webapp.controller.common import header_checker, response, response_code
from webapp.models import menus


def create_item(request):
    new_item = menus.Menu.objects.create()
    new_item.save()
    return response(response_code['OK'], new_item)


def get_menus(request):
    item_id = header_checker(request)
    item = menus.Menu.objects.all()
    return response(response_code['OK'], item)



def modify_menu_item(request):
    item_id = header_checker(request)
    item = menus.Menu.objects.filter(item_id)
    req = request.POST
    new_name=req.get('new_name')
    new_price=req.get('new_price')
    new_offset=req.get('new_offset')
    new_status=req.get('new_status')
    item.name=new_name
    item.price=new_price
    item.offset=new_offset
    item.status=new_status
    item.save()
    return response(response_code['OK'])


def remove_menu_item(request):
    item_id = header_checker(request)
    item = menus.Menu.objects.filter(item_id)
    item.delete()
    return response(response_code['OK'])
