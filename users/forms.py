from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль' ,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')