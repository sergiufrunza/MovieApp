from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.core.validators import validate_email
from django.contrib.auth.forms import User
from .models import *


class EditFormProfile(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}), validators=[validate_email])
    user_name = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    avatar = forms.ImageField(label='Profile Photo', widget=forms.FileInput(attrs={'class': 'avatar_in'}))
    field_order = ['user_name', 'email' , 'avatar']

    class Meta:
        model = UserProfile
        fields = ['user_name', 'email' , 'avatar']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login' ,widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email' ,widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password1' ,
                                widget=forms.PasswordInput(attrs={'class': 'form-input' ,'id': 'password'}))
    password2 = forms.CharField(label='Password2' ,
                                widget=forms.PasswordInput(attrs={'class': 'form-input' ,'id': 'password'}))
    field_order = ['username' ,'email' ,'password1' ,'password2']

    class Meta:
        model = User
        fields = {'username' ,'email' ,'password1' ,'password2'}


class AuthForm(AuthenticationForm):
    username = forms.CharField(label='Login' ,widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password' ,
                               widget=forms.PasswordInput(attrs={'class': 'form-input' ,'id': 'password'}))
    field_order = ['username' ,'password']

    class Meta:
        model = User
        fields = {'username' ,'password'}
