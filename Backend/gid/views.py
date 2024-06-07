from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from gid.forms import UserLoginForm, UserRegistrationForm
from gid.models import Sight


def index(request):
    context = {
        'sights': Sight.objects.all()[:4],
    }
    return render(request, 'gid/index.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'gid/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'gid/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))