from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.Proxy import menus
from webapp.controller.common import header_checker, response, response_code


def test_api(request):
    return JsonResponse({'foo': 'bar'})


def post_api(request):
    if (header_checker(request)):
        print('11', request.POST.get('name'))
        menus_info = menus.create(request.POST.get('name'))
        print(menus_info)
        return response(response_code['OK'], menus_info)
