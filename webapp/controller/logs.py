from webapp.controller.common import header_checker, response, response_code
from webapp.models import logs

def create_log(request):
    new_log=logs.Log.objects.create()
    log_id=new_log.log_id
    return response(response_code['OK'],log_id)


def get_logs(request):
    worker_id = header_checker(request)
    log=logs.Log.get(worker_id=worker_id)
    return response(response_code['OK'],log)
