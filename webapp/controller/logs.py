from webapp.controller.common import header_checker, response, response_code


def create_log(request):
    return response(response_code['OK'])


def get_logs(request):
    return response(response_code['OK'])
