from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2']
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class LoginForm(AuthenticationForm):
    pass
