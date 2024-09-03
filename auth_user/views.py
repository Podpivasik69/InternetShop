from django.shortcuts import render, redirect
from django.contrib import messages
from auth_user.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Создание профиля
            Profile.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                patronymic=form.cleaned_data.get('patronymic'),
                birth_date=form.cleaned_data.get('birth_date'),
                avatar=form.cleaned_data.get('avatar')
            )
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return render(request , template_name='users/logout.html')
