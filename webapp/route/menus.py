from django.conf.urls import include
from django.urls import path
from webapp.controller import menus

urlpatterns = [
    path('test', menus.test_api, name='menuTest')
]

