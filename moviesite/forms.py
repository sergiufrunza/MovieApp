from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.forms import User
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login' ,widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email' ,widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password1' ,
                                widget=forms.PasswordInput(attrs={'class': 'form-input pass' ,'id': 'pass1'}))
    password2 = forms.CharField(label='Password2' ,
                                widget=forms.PasswordInput(attrs={'class': 'form-input pass' ,'id': 'pass2'}))
    field_order = ['username' ,'email' ,'password1' ,'password2']

    class Meta:
        model = User
        fields = {'username' ,'email' ,'password1' ,'password2'}


class AuthForm(AuthenticationForm):
    username = forms.CharField(label='Login' ,widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password' ,
                               widget=forms.PasswordInput(attrs={'class': 'form-input pass' ,'id': 'pass1'}))
    field_order = ['username' ,'password']

    class Meta:
        model = User
        fields = {'username' ,'password'}

#
# class ProfileDate(forms.ModelForm):
#     user_name = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     avatar = forms.ImageField(label='Profile Photo', widget=forms.FileInput(attrs={'class': 'avatar_in'}))
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user_status'].empty_label = "Default"
#         self.fields['user_status'].label = "User Status"
#         self.fields['user_status'].widget.attrs = {'class': 'form-select'}
#
#
#
#     class Meta:
#         model = UserProfile
#         fields = ['user_name', 'user_status', 'avatar']

# class AddMovies(forms.ModelForm):
#     name = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea(attrs={'col': 60, 'row': 60}))
#     slug = forms.SlugField(max_length=100)
#     cover = forms.ImageField()
#     movie = forms.FileField()
#     art = forms.ImageField()
#     year = forms.ModelChoiceField(queryset=Years.objects.all())
#     country = forms.ModelChoiceField(queryset=Countries.objects.all())
#     category = forms.ModelChoiceField(queryset=Categories.objects.all())
#     film_director = forms.ModelChoiceField(queryset=FilmDirectors.objects.all())
#
#     class Meta:
#         model = Movie
