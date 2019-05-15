from webapp.controller.common import header_checker, response, response_code
from webapp.models import persons


def login(request):
     return response(response_code['OK'])


def get_self_info(id):
    user = persons.Person.findBy(id)
    if (user):
        return response(response_code['OK'], user)
    return response(response_code['BAD_REQUEST'])


def set_self_info(request):
    req = request.POST
    person_id = req.get('person_id')
    worker_id = req.get('worker_id')
    name = req.get('name')
    address = req.get('address')
    phone = req.get('phone')
    position = req.get('position')
    password = req.get('password')
    user=persons.Person.objects.filter(person_id=person_id)
    user.worker_id=worker_id
    user.name=name
    user.address=address
    user.address=phone
    user.position=position
    user.password=password
    user.save()
    return response(response_code['OK'])


def get_all_info(request):
    person_id = header_checker(request)
    if(person_id>1):
        users=persons.Person.objects.all.get()
        return response(response_code['OK'],users)
    else:
        return response(response_code['BAD_REQUEST'])

def change_password(request):
    person_id = header_checker(request)
    req = request.POST
    old_password=req.get('old_password')
    new_password=req.get('new_password')
    user=persons.Person.objects.filter(person_id=person_id)
    if(user.password==old_password):
      user.password=new_password
      user.save
      return response(response_code['OK'])
    else:
        return response(response_code['BAD_REQUEST'])



