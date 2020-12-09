from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from user.models import User


# /register/
def register(request):
    """注册View视图函数"""
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)

        return JsonResponse({'message': '注册成功'})


def login(request):
    username = request.session.get('username')
    if username:
        return HttpResponse('%s用户已登录' % username)
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remeber = request.POST.get('remeber')
        try:
            user = User.objects.get(username=username, password=password)

        except User.DoesNotExist:
            return JsonResponse({'message': '登录错误'})
        else:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if remeber != 'ture':
                request.session.set_expiry(0)
            return JsonResponse({'message': '登录成功'})

