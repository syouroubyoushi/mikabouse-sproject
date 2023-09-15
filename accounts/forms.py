from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser
from .models import Comment

#会員登録フォーム
class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2']

#ログインフォーム
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#comment機能
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","email","body"]
