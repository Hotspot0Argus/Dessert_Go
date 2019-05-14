from django.urls import path
from webapp.controller import persons

urlpatterns = [
    path('logout', persons.login, name='logout'),

    path('get_self_info', persons.get_self_info, name='get_self_info'),
    path('set_self_info', persons.set_self_info, name='set_self_info'),
    # admin
    path('get_all_info', persons.get_all_info, name='get_all_info'),

    path('change_password', persons.change_password, name='change_password')


]
