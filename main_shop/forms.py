from dataclasses import field
from logging import PlaceHolder
from statistics import mode
from tkinter import Widget
from turtle import textinput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача(Nickname)", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label="Старий пароль" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label="Новий пароль" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Повторіть новий пароль" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')

class UserDataChangeForm(UserChangeForm): 
    username = forms.CharField(label="Ім'я користувача(Nickname)" , widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Справжнє ім'я" , widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Е-почта" , widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','email')


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Ім'я користувача(Nickname)" , widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Справжнє ім'я" , widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Е-почта" , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 =  forms.CharField(label="Пароль" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =  forms.CharField(label="Повторіть пароль" , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name','email','password1','password2')
