from django.conf.urls import include
from django.urls import path
from webapp.controller import menus


urlpatterns = [
    # Test api
    path('test', menus.test_api, name='test_api'),
    path('post', menus.post_api, name='post_api'),
    path('menu/', include('webapp.routes.menus'), name='post_api')
]

