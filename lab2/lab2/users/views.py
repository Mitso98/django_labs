from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def login_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('polls')
        else:
            messages.success(req, ('There Was An Error Try Again!'))
            return redirect('login_user')
    else:
        return render(req, 'users/login.html', {})


def logout_user(req):
    logout(req)
    messages.success(req, 'You were logged out!')
    return redirect('login_user')


def register_user(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(req, user)
            messages.success(req, ('Regestration success'))
            return redirect('polls')
    else:
        form = UserCreationForm()
    return render(req, 'users/register_user.html', {
        'form': form
    })
