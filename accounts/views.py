from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def regist(request):
    return render(request, 'regist.html')
#login
def login(request):
    return render(request, 'login.html')
