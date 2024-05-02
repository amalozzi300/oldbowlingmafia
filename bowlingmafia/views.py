from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bowlingmafia.utils import get_login_status

def home(request):
    context = {'logged_in': get_login_status(request)}
    return redirect('/tournaments')

def login_view(request):
    context = {'login_view': 'active'}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid credentials.')

    return render(request, 'bowlingmafia/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')