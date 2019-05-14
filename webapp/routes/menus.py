from django.urls import path
from webapp.controller import menus

urlpatterns = [
    path('create', menus.create_item, name='create_item'),

    path('get_menus', menus.get_menus, name='get_menus'),
    path('modify_menu/<int:menu_id>', menus.modify_menu_item, name='modify_menu_item'),

    path('remove_menu/<int:menu_id>', menus.remove_menu_item, name='remove_menu_item')
]
