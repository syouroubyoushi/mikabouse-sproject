from django.contrib import admin
from django.urls import path
from accounts.views import index
from accounts.views import regist
from accounts.views import regista
from accounts.views import check_username
from accounts.views import login

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('regist/', regist, name='regist'),
    path('regist/regista/', regista, name='regista'),
    path('login/', login, name='login'),
    path('regist/check_username/', check_username, name='check_username'),
]