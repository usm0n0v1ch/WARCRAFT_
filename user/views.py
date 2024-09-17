from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from user.forms import RegisterForm, LoginForm


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('about')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')

    form = RegisterForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('about')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('about')
            else:
                return redirect('login')

    form = LoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


def log_out(request):
    logout(request)
    return redirect('login')
