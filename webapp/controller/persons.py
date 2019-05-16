from webapp.controller.common import header_checker, response, response_code
from webapp.models import persons
from django.core import serializers


def create(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        person = persons.Person.create()
        worker_id = req.get('worker_id')
        res = persons.Person.find_by_worker_id(worker_id)
        if not res:
            name = req.get('name')
            address = req.get('address')
            phone = req.get('phone')
            position = req.get('position')
            person.worker_id = worker_id
            person.name = name
            person.address = address
            person.phone = phone
            person.position = position
            person.save()
            return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_self_info(request):
    user = header_checker(request)
    if user:
        return response(response_code['OK'],
                        {'person_id': user.person_id, 'worker_id': user.worker_id, 'name': user.name,
                         'phone': user.phone, 'address': user.address})
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


def remove_other(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        worker_id = req.get('worker_id')
        other = persons.Person.find_by_worker_id(worker_id)
        other.delete()
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def set_others_info(request):
    user = header_checker(request)
    if user and user.position > 1:
        req = request.POST
        worker_id = req.get('worker_id')
        other = persons.Person.find_by_worker_id(worker_id)
        name = req.get('name')
        address = req.get('address')
        phone = req.get('phone')
        position = req.get('position')
        other.name = name
        other.address = address
        other.phone = phone
        other.position = position
        other.save()
        return response(response_code['OK'])
    return response(response_code['BAD_REQUEST'])


def get_all_info(request):
    user = header_checker(request)
    if user and (user.position > 1):
        users = persons.Person.find_all_person_info()
        return response(response_code['OK'], serializers.serialize('json', users))
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
