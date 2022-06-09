from django.forms import ModelForm
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

