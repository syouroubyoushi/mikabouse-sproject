from django.contrib import admin
from django.urls import path
from accounts.views import index,regist,regista,deleteacc,change_password,check_username,login,home

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),#admin/というURLでadmin.site.urlsにアクセスできる
    path('', index, name='index'),
    path('regist/', regist, name='regist'),
    path('regist/regista/', regista, name='regista'),
    path('delete/', deleteacc, name='delete'),
    path('change/', change_password, name='change'),
    path('login/', login, name='login'),
    path('regist/check_username/', check_username, name='check_username'),
    path('home/',home,name='home'),
]