from django.http import JsonResponse
<<<<<<< HEAD
import json
# from jwt import (
#     JWT,
#     jwk_from_dict,
#     jwk_from_pem,
# )


def header_checker(req):
    # session = req.META.get("HTTP_SESSION")
    # if session:
    #     jwt = JWT()
    #     # token = jwt.encode(payload, 'secret', algorithm='HS256')
    #     try:
    #         jwt.verify(session, 'gjwAq;JwqSDergEOkg')
    #     except:
    #         return False
    #     # 获取user 判断session是否正确
    #     return True
    # else:
      return 5
=======
from django.http import HttpResponse
from webapp.models import persons
import jwt


def header_checker(req):
    session = req.META.get("HTTP_AUTHORIZATION")
    print(req.META)
    if session:
        user = jwt.decode(session, 'gjwAq;JwqSDergEOkg')
        # 数据库中找 worker_id 和 person_id 对上的话就行
        result = persons.Person.check_worker_id_and_person_id(user['person_id'], user['worker_id'])
        # 获取user 判断session是否正确
        if result:
            return user['person_id']
    else:
        return -1
>>>>>>> d09e173cf20fd0e79c8a0f508b62a8c2eb1f2dba


def response(code, message=''):
    print(message)
    mess = {'status': code, 'data': message}
    return JsonResponse(mess)


response_code = {'OK': 200,
                 'CREATED': 201,
                 'NO_CONTENT': 204,
                 'NOT_MODIFIED': 304,
                 'BAD_REQUEST': 400,
                 'UNAUTHORIZED': 401,
                 'FORBIDDEN': 403,
                 'NOT_FOUND': 404,
                 'METHOD_NOT_ALLOWED': 405,
                 'GONE': 410,
                 'UNSUPPORTED_MEDIA_TYPE': 415,
                 'UNPROCESSABLE_ENTITY': 422,
                 'TOO MANY REQUESTS': 429,
                 'INTERNAL_ERROR': 500}
