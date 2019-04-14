# buffer
from webapp.models import Menu


def get_by_id():
    return Menu.objects.all()


def create(name):
    menu = Menu.objects.create(name=name, price=10)
    return menu.get_obj()
