from django.http import JsonResponse
import json
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)


def header_checker(req):
    session = req.META.get("HTTP_SESSION")
    if session:
        jwt = JWT()
        # token = jwt.encode(payload, 'secret', algorithm='HS256')
        try:
            jwt.verify(session, 'gjwAq;JwqSDergEOkg')
        except:
            return False
        # 获取user 判断session是否正确
        return True
    else:
        return False


def response(code, message):
    return JsonResponse({'message': message}, status=code)


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