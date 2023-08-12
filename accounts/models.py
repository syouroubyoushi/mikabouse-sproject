from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#ユーザー情報
class CustomUser(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    email = models.EmailField(unique=True)

#投稿
class Text(models.Model):
    text=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    reply_to = models.IntegerField(null=True)

# DM
class DM(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    message_partner = models.IntegerField(null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)