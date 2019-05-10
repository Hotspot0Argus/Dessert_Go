#buffer
from webapp.models import MenuInfo
from django.http import JsonResponse

def get_by_id():
    return MenuInfo.objects.all()


def create(name,price):
    menu=MenuInfo.objects.create(name=name,price=price)
    return menu.get_obj()


def delete(name):
   list = MenuInfo.objects.filter(name=name).delete()
   return 0


def update(name,newname,newprice):
    MenuInfo.objects.filter(name=name).update(name=newname,price=newprice)
    menu={"newname":newname,"newprice":newprice}
    return  menu


def query(name):

    menu = MenuInfo.objects.get(name=name)
    return menu.get_obj()
