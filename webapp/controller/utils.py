from webapp.controller.common import header_checker, response, response_code
from webapp.models import persons
from webapp.models import logs

import jwt


def login(request):
    req = request.POST
    worker_id = req.get('worker_id')
    password = req.get('password')
    user_info = persons.Person.login(worker_id, password)
    # 数据库处理
    payload = {
        'worker_id': user_info.worker_id,
        'person_id': user_info.person_id,
        'position': user_info.position,
    }
    token = jwt.encode(payload, 'gjwAq;JwqSDergEOkg', algorithm='HS256')
    logs.Log.create(order_id=None, person_id=user_info.person_id, person_name=user_info.name)
    return response(response_code['OK'], {'token': str(token, encoding="utf-8"), 'info': payload})


def logout(request):
    user = header_checker(request)
    if user:
        logs.Log.change_log(person_id=user.person_id)
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def verify(request):
    user = header_checker(request)
    if user:
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])
