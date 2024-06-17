from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from gid.forms import UserLoginForm, UserRegistrationForm, RatingForm, UserNoteForm, CommentForm
from gid.models import Sight, Comment, UserNote, Visit, Rating


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

from django.contrib import messages

def sight_detail(request, sight_id):
    sight = get_object_or_404(Sight, pk=sight_id)
    form = RatingForm()
    note_form = UserNoteForm()
    comments = Comment.objects.filter(sight=sight)
    user_note = None

    # Проверяем, посещал ли пользователь это место
    user_visited = False
    if request.user.is_authenticated:
        user_visited = Visit.objects.filter(user=request.user, sight=sight).exists()

    if request.user.is_authenticated:
        user_note = UserNote.objects.filter(sight=sight, user=request.user).first()
        if request.method == 'POST':
            if 'rating' in request.POST:
                form = RatingForm(request.POST)
                if form.is_valid():
                    rating, created = Rating.objects.update_or_create(
                        sight=sight, user=request.user,
                        defaults={'score': form.cleaned_data['score']}
                    )
                    return redirect('sight_detail', sight_id=sight.id)
            elif 'note' in request.POST:
                note_form = UserNoteForm(request.POST, instance=user_note)
                if note_form.is_valid():
                    note = note_form.save(commit=False)
                    note.sight = sight
                    note.user = request.user
                    note.save()
                    return redirect('sight_detail', sight_id=sight.id)

    return render(request, 'gid/sight_detail.html', {
        'sight': sight,
        'form': form,
        'note_form': note_form,
        'comments': comments,
        'user_note': user_note,
        'user_visited': user_visited,
    })


@login_required
def submit_comment(request, sight_id):
    sight = get_object_or_404(Sight, pk=sight_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.sight = sight
            comment.user = request.user
            comment.save()
            return redirect('sight_detail', sight_id=sight_id)
    else:
        form = CommentForm()
    return render(request, 'gid/sight_detail.html', {'form': form, 'sight': sight})

@login_required
def mark_visited(request, sight_id):
    if request.method == 'POST':
        sight = get_object_or_404(Sight, pk=sight_id)
        Visit.objects.get_or_create(user=request.user, sight=sight)
        return redirect('sight_detail', sight_id=sight_id)


@login_required
def user_visited_sights(request):
    visited_sights = Visit.objects.filter(user=request.user)
    return render(request, 'gid/user_visited_sights.html', {'visited_sights': visited_sights})
