from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.Proxy import menusProxy
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return render(request, 'webapp/index.html', {})


@csrf_exempt
def test_api(request):
    return JsonResponse({'foo': 'bar'})


@csrf_exempt
def post_api(request):
    print('11', request.POST.get('name'))
    menus_info=menusProxy.create(request.POST.get('name'),request.POST.get('price'))
    print(menus_info)
    return JsonResponse(menus_info)


@csrf_exempt
def delete_api(request):
    # print('11', request.POST.get('name'))
    menus_info=menusProxy.delete(request.POST.get('name'))
   # print(menus_info)
    return JsonResponse({"menus_info":menus_info})


@csrf_exempt
def update_api(request):
    try:
        # print('11', request.POST.get('name'))
        menus_info=menusProxy.update(request.POST.get('name'),request.POST.get('newname'),request.POST.get('newprice'))
        print(menus_info)
        #return JsonResponse(menus_info)
       # return JsonResponse(menus_info)
        return JsonResponse(menus_info)
    except:
          return JsonResponse({"MSg":"error"})

@csrf_exempt
def query_api(request):


        # print('11', request.POST.get('name'))
        menus_info=menusProxy.query(request.POST.get('name'))
        print(menus_info)
        #return JsonResponse(menus_info)
        # return JsonResponse(menus_info)
       # return JsonResponse(menus_info)s
        return  JsonResponse(menus_info)



