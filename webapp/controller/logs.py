from webapp.controller.common import header_checker, response, response_code
from webapp.models import logs
from django.core import serializers


def create_log(request):
    req = request.POST
    order_id = req.get('order_id')
    worker_id = req.get('worker_id')
    logs.Log.new_log_create(order_id, worker_id)
    return response(response_code['OK'])


def change_log(request):
    user = header_checker(request)
    if user:
        logs.Log.change_log(user['person_id'])
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_logs(request):
    user = header_checker(request)
    if user and user.position > 1:
        all_log = logs.Log.find_logs()
        return response(response_code['OK'], serializers.serialize('json', all_log))
    return response(response_code['BAD_REQUEST'])
