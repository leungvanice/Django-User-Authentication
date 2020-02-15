from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='')
    email = forms.EmailField(label='')
    password = forms.CharField(
        max_length=32, label='', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ('username')
        self.fields['email'].widget.attrs['placeholder'] = ('email')
        self.fields['password'].widget.attrs['placeholder'] = ('password')


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='')
    # password = forms.PasswordInput()
    password = forms.CharField(widget=forms.PasswordInput(), label='')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = ('email')
        self.fields['password'].widget.attrs['placeholder'] = ('password')
