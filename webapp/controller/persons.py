from webapp.controller.common import header_checker, response, response_code


def login(request):
    return response(response_code['OK'])


def get_self_info(request):
    return response(response_code['OK'])


def set_self_info(request):
    return response(response_code['OK'])


def get_all_info(request):
    return response(response_code['OK'])


def change_password(request):
    return response(response_code['OK'])
