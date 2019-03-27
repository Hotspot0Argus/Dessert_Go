from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return render(request, 'webapp/index.html', {})


@csrf_exempt
def test_api(request):
    return JsonResponse({'foo': 'bar'})


@csrf_exempt
def post_api(request):
    print('11', request.POST.get('name'))
    return JsonResponse({'foo': '1111'})
