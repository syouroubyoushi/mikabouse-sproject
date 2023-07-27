from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password


#トップページ
def index(request):
    return render(request, 'index.html')

#会員登録
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None) 
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        
        err_data={}
        if not(username and email and password1 and password2):
            err_data['error'] = ''
        
        elif password1 != password2:
            err_data['error'] = ''
        
        else:
            user = User(
                username=username,
                email=email,
                password=make_password(password1),
            )
            user.save()

    return HttpResponseRedirect('regista')
    
def checkname(request):
    try:
        user = User.objects.get(username=request.GET['username'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def regista(request):
    return render(request, 'regista.html')

#ろぐいん
def login(request):
    return render(request, 'login.html')
