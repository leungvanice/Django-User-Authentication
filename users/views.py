from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email)

            user.set_password(password)
            user.save()
            return redirect('home')
    else:
        form = forms.UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data.get('email')
            form_password = form.cleaned_data.get('password')
            theusername = User.objects.get(email=form_email).username

            user = authenticate(
                request, username=theusername, password=form_password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("Invalid Data")

    else:
        form = forms.UserLoginForm()
    return render(request, 'users/login.html', {'form': form})
