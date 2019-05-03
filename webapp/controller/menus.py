from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.Proxy import menus


def test_api(request):
    return JsonResponse({'foo': 'bar'})


def post_api(request):
    print('11', request.POST.get('name'))
    menus_info = menus.create(request.POST.get('name'))
    print(menus_info)
    return JsonResponse(menus_info)
