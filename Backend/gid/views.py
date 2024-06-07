from django.shortcuts import render


def login(request):
    return render(request, 'gid/login.html')

def register(request):
    return render(request, 'gid/register.html')