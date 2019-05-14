from webapp.controller.common import header_checker, response, response_code


def create_item(request):
    return response(response_code['OK'])


def get_menus(request):
    return response(response_code['OK'])


def modify_menu_item(request):
    return response(response_code['OK'])


def remove_menu_item(request):
    return response(response_code['OK'])
