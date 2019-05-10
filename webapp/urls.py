from django.conf.urls import include
from django.urls import path
from webapp.controller import menus

urlpatterns = [
    path('$', menus.index, name='index'),

    # Test api
    path('post', menus.post_api, name='post_api'),
    path('delete', menus.delete_api, name='delete_api'),
    path('update', menus.update_api, name='update_api'),
    path('query', menus.query_api, name='query_api'),
    path('menu/', include('webapp.route.menus'), name='post_api')
]

