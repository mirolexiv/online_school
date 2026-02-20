from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from lessons import views
from users.forms import LoginForm, RegisterUserForm

menu=views.menu
sidebar=views.sidebar


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect ('lessons:about')
    else:
        form = LoginForm()
    context = {'form': form, 'sidebar': sidebar, 'menu': menu}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect(reverse('lessons:about'))

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()   # створює користувача
            login(request, user) # автоматично логінить
            return redirect('lessons:about')
    else:
        form = RegisterUserForm()

    context = {'form': form,'sidebar': sidebar,'menu': menu }
    return render(request, 'users/register.html', context)