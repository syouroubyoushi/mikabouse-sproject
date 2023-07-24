from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

#トップページ
def index(request):
    return render(request, 'index.html')

#会員登録
def regist(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
    return render(request, 'regist.html')

#ろぐいん
def login(request):
    return render(request, 'login.html')
