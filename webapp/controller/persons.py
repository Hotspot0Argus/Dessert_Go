from webapp.controller.common import header_checker, response, response_code
from webapp.models import persons


def login(request):
    return response(response_code['OK'])


def get_self_info(request):
    person_id = header_checker(request)
    req = request.POST
    user = persons.Person.find_by_person_id(person_id)
    if user:
        return response(response_code['OK'], user)
    return response(response_code['BAD_REQUEST'])


def set_self_info(request):
    person_id = header_checker(request)
    req = request.POST
    worker_id = req.get('worker_id')
    name = req.get('name')
    address = req.get('address')
    phone = req.get('phone')
    user = persons.Person.find_by_person_id(person_id)
    user.worker_id = worker_id
    user.name = name
    user.address = address
    user.address = phone
    user.save()
    return response(response_code['OK'])


def get_all_info(request):
    person_id = header_checker(request)
    req = request.POST
    position = req.get('position')
    if position > 1:
        users = persons.Person.find_all_person_info()
        return response(response_code['OK'], users)
    else:
        return response(response_code['BAD_REQUEST'])


def change_password(request):
    person_id = header_checker(request)
    req = request.POST
    old_password = req.get('old_password')
    new_password = req.get('new_password')
    user = persons.Person.find_by_person_id()
    # (
    if  user.password == old_password:
        user.password = new_password
        user.save()
        return response(response_code['OK'])
    else:
        return response(response_code['BAD_REQUEST'])
