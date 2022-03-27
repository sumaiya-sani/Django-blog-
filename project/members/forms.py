from dataclasses import field
import email
from unittest.util import _MAX_LENGTH
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

from myblog.models import Post


class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)

    class Mata:
        models=User
        fields=('username','first_name','last_name','email','password1','password2')


class EditForm(UserChangeForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    last_login=forms.CharField(max_length=255)
    password=forms.CharField(max_length=100)

    class Mata:
        models=User
        fields=('username','first_name','last_name','last_login','password',)


  
class LoginForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('username','password')      
