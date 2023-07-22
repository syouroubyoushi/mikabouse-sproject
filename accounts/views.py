from django.shortcuts import render

#トップページ
def index(request):
    return render(request, 'index.html')

#会員登録
def regist(request):
    return render(request, 'regist.html')

#ろぐいん
def login(request):
    return render(request, 'login.html')
