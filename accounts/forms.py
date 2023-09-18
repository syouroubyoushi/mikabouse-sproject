from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser
from .models import Comment,Profile

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

#プロフィール編集
class ProfileForm(forms.ModelForm):
    introduction_text = forms.CharField(required=False)
    location = forms.CharField(required=False)
    birth_month = forms.ChoiceField(choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 13)],required=False)
    birth_day = forms.ChoiceField(choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 32)],required=False)
    birth_year = forms.ChoiceField(choices=[(str(i).zfill(4), str(i).zfill(4)) for i in range(1900, 2022)],required=False)

    class Meta:
        model = Profile
        fields = ['introduction_text','location', 'birth_month', 'birth_day', 'birth_year']