from webapp.controller.common import header_checker, response, response_code
from webapp.models import persons


def create(request):
    user = header_checker(request)
    if user & user.position > 1:
        person_id = persons.Person.create()
        return response(response_code['OK'], person_id)


def get_self_info(request):
    user = header_checker(request)
    if user:
        return response(response_code['OK'], user)
    return response(response_code['BAD_REQUEST'])


def set_self_info(request):
    user = header_checker(request)
    if user:
        req = request.POST
        name = req.get('name')
        address = req.get('address')
        phone = req.get('phone')
        user.name = name
        user.address = address
        user.phone = phone
        user.save()
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_all_info(request):
    user = header_checker(request)
    req = request.POST
    if user & user.position > 1:
        users = persons.Person.find_all_person_info()
        return response(response_code['OK'], users)
    else:
        return response(response_code['BAD_REQUEST'])


def change_password(request):
    user = header_checker(request)
    if user:
        req = request.POST
        old_password = req.get('old_password')
        new_password = req.get('new_password')
        if user.password == old_password:
            user.password = new_password
            user.save()
            return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])
