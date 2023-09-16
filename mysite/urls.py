from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import index,regist,deleteacc,change_password,check_username,user_login,home,profile,Delete,user_logout

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),#admin/というURLでadmin.site.urlsにアクセスできる
    path('', index, name='index'),
    path('regist/', regist, name='regist'),
    path('logout/', user_logout, name='logout'),
    path('delete/', deleteacc, name='delete'),
    path('change/', change_password, name='change'),
    path('login/', user_login, name='user_login'),
    path('regist/check_username/', check_username, name='check_username'),
    path('home/',home,name='home'),
    path('home/<int:text_id>/Delete/',Delete,name='Delete'),
    path('profile/',profile,name='profile'),
]