from webapp.controller.common import header_checker, response, response_code
from webapp.models import logs


def create_log(request):
    new_log = logs.Log.new_log_create()
    new_log_id = new_log.log_id
    return response(response_code['OK'], new_log_id)


def get_logs(request):
    person_id = header_checker(request)
    log = logs.Log.find_logs(person_id)
    return response(response_code['OK'], log)
