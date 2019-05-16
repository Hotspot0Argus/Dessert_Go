from webapp.controller.common import header_checker, response, response_code
from webapp.models import logs


def create_log(request):
    req = request.POST
    order_id = req.get('order_id')
    person_id = req.get('person_id')
    logs.Log.new_log_create(order_id, person_id)
    return response(response_code['OK'])


def change_log(request):
    user = header_checker(request)
    if user:
        logs.Log.change_log(user['person_id'])
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_logs(request):
    user = header_checker(request)
    if user & user.positon > 1:
        all_log = logs.Log.find_logs()
        return response(response_code['OK'], all_log)
    return response(response_code['BAD_REQUEST'])
