from django.forms import ModelForm, Form
from django import forms
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class AuthorizationForm(ModelForm):
    class Meta:
        model = Authorization
        fields = ['user', 'file', 'autorization']

class LoginForm(Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=128)