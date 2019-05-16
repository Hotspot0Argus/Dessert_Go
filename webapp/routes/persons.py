from django.urls import path
from webapp.controller import persons

urlpatterns = [
    path('create', persons.create, name='create'),
    path('get_self_info', persons.get_self_info, name='get_self_info'),
    path('set_self_info', persons.set_self_info, name='set_self_info'),
    path('get_all_info', persons.get_all_info, name='get_all_info'),
    path('set_others_info', persons.set_others_info, name='set_others_info'),
    path('remove_other', persons.remove_other, name='remove_other'),

    path('change_password', persons.change_password, name='change_password')

]
