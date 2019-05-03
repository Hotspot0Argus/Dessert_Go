def check_post(request, name):
    return request.POST.get(name)


def check_get(request, name):
    return request.GET.get(name)
