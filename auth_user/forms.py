from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    patronymic = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'birth_date', 'avatar']
