from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('$', views.index, name='index'),

    # Test api
    path('api/test', views.test_api, name='test_api'),
    path('api/post', views.post_api, name='post_api')
]

