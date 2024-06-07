from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from gid.forms import UserLoginForm, UserRegistrationForm, RatingForm
from gid.models import Sight, Rating


def index(request):
    top_sights = Sight.top_rated_sights()
    return render(request, 'gid/index.html', {'top_sights': top_sights})

def catalog(request):
    context = {
        'sights': Sight.objects.all(),
    }
    return render(request, 'gid/catalog.html', context)

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

def sight_detail(request, sight_id):
    sight = get_object_or_404(Sight, pk=sight_id)
    form = RatingForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RatingForm(request.POST)
            if form.is_valid():
                rating, created = Rating.objects.update_or_create(
                    sight=sight, user=request.user,
                    defaults={'score': form.cleaned_data['score']}
                )
                return redirect('sight_detail', sight_id=sight.id)
        else:
            return redirect('login')  # Перенаправить на страницу входа, если пользователь не аутентифицирован

    return render(request, 'gid/sight_detail.html', {'sight': sight, 'form': form})