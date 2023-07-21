from django.contrib import admin
from django.urls import path
from accounts.views import index
from accounts.views import regist

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('regist/', regist, name='regist'),
]