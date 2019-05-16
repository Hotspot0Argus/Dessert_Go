from django.urls import path
from webapp.controller import utils

urlpatterns = [
    path('login', utils.login, name='login'),
    path('verify', utils.verify, name='login')
]
