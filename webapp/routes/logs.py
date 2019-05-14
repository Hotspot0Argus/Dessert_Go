from django.urls import path
from webapp.controller import logs

urlpatterns = [
    path('create', logs.create_log, name='create_log'),

    path('get_logs', logs.get_logs, name='get_logs')
]
