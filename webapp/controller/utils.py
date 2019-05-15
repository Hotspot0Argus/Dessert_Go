from webapp.controller.common import header_checker, response, response_code
# from jwt import JWT
#
#
def login(request):
    req = request.POST
    worker_id = req.get('worker_id')
    password = req.get('password')
#     # 数据库处理
#     jwt = JWT()
#     payload = {
#         'worker_id': '201902138',
#         'position': 1,
#         'person_id': 12
#     }
#     token = jwt.encode(payload, 'secret', algorithm='HS256')
#     return response(response_code['OK'], {'token': token})
