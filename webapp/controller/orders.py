from webapp.controller.common import header_checker, response, response_code


def create(request):
    return response(response_code['OK'])


def get_order(request):
    return response(response_code['OK'])


def modify_order(request):
    return response(response_code['OK'])


def finish_order(request):
    return response(response_code['OK'])


def get_orders(request):
    return response(response_code['OK'])
