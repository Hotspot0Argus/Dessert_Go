from webapp.controller.common import header_checker, response, response_code
<<<<<<< HEAD
# from jwt import JWT
#
#
=======
import jwt


>>>>>>> d09e173cf20fd0e79c8a0f508b62a8c2eb1f2dba
def login(request):
    req = request.POST
    worker_id = req.get('worker_id')
    password = req.get('password')
<<<<<<< HEAD
#     # 数据库处理
#     jwt = JWT()
#     payload = {
#         'worker_id': '201902138',
#         'position': 1,
#         'person_id': 12
#     }
#     token = jwt.encode(payload, 'secret', algorithm='HS256')
#     return response(response_code['OK'], {'token': token})
=======
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
>>>>>>> d09e173cf20fd0e79c8a0f508b62a8c2eb1f2dba
