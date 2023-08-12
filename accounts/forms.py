from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser

#会員登録フォーム
class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2','email']

#ログインフォーム
class LoginForm(AuthenticationForm):
    pass
