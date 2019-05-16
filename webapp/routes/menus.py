from django.urls import path
from webapp.controller import menus

urlpatterns = [
    path('create', menus.create_item, name='create_item'),

    path('get_menu', menus.get_menu, name='get_menu'),
    path('get_menus', menus.get_menus, name='get_menus'),
    path('get_menus_on_sell', menus.get_menus_on_sell, name='get_menus_on_sell'),
    path('modify_menu', menus.modify_menu_item, name='modify_menu_item'),

    path('remove_menu', menus.remove_menu_item, name='remove_menu_item')
]
