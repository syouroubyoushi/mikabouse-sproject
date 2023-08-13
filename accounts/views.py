from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password
from accounts.models import Text

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
        user = User(
            username=username,
            email=email,
            password=make_password(password1),
        )
        user.save()
        return HttpResponseRedirect('regista')
    
#会員登録の時IDが重複かをLIVEで確認
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', '').strip()
        if not username:
            return JsonResponse({'result': 'error', 'message': 'IDを入力してください。'})
        users = User.objects.filter(username=username)
        if users.exists():
            return JsonResponse({'result': 'success', 'message': '使用できないIDです。','idck': False})
        else:
            return JsonResponse({'result': 'success', 'message': '使用可能なIDです.','idck': True})

def regista(request):
    return render(request, 'regista.html')

#ろぐいん
def login(request):
    return render(request, 'login.html')

#ホームページ
def home(request):
    toukou = Text.objects.all
    if request.method =='POST':
        text = request.POST.get('text',None)
        m = Text(text= text)#ここでつくった変数をTextというデータベースモデルに保存
        m.save()
    return render(request,'home.html',{'Text':toukou})
