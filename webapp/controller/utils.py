from webapp.controller.common import header_checker, response, response_code
import jwt


def login(request):
    req = request.POST
    worker_id = req.get('worker_id')
    password = req.get('password')
    # 数据库处理
    payload = {
        'worker_id': '201902138',
        'position': 1,
        'person_id': 12
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return response(response_code['OK'], {'token': token})
