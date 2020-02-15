from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
# Create your views here.


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