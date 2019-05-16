from webapp.controller.common import header_checker, response, response_code
import jwt


def login(request):
    req = request.POST
    worker_id = req.get('worker_id')
    password = req.get('password')

    # 数据库处理
    payload = {
        'worker_id': '201902138',
        'person_id': 123,
        'position': 1,
    }
    token = jwt.encode(payload, 'gjwAq;JwqSDergEOkg', algorithm='HS256')
    return response(response_code['OK'], {'token': str(token, encoding="utf-8"), 'info': payload})


def verify(request):
    person_id = header_checker(request)
    if person_id >= 0:
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])
