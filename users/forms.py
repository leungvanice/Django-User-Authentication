from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=32) 


class UserLoginForm(forms.Form): 
    email = forms.EmailField() 
    # password = forms.PasswordInput() 
    password = forms.CharField(widget=forms.PasswordInput())