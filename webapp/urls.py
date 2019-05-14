from django.conf.urls import include
from django.urls import path
from webapp.controller import menus


urlpatterns = [
    path('session/',include('webapp.routes.utils'), name='session'),
    path('orders/', include('webapp.routes.orders'), name='orders'),
    path('menus/', include('webapp.routes.menus'), name='menus'),
    path('persons/', include('webapp.routes.persons'), name='persons'),
    path('logs/', include('webapp.routes.logs'), name='logs')
]

