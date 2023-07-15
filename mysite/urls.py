from django.contrib import admin
from django.urls import path
from accounts.views import index

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]