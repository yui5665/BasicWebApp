from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from os import listdir
from .models import User, File

# Create your views here.
def index(Request):
    print(Request.user)
    return HttpResponse("Hello world!")

def storage(Request):
    return HttpResponse(listdir('backend/storage/'))

def details(Request):
    obj = File.objects.get(id=1)
    my_context = {'object' : obj}
    return render(Request, 'backend/storage/details.html', my_context)

def register_file(Request):
    form = FileForm(Request.POST or None)
    if form.is_valid():
        form.save()
    my_context = {'form' : form}
    return render(Request, 'backend/storage/register_file.html', my_context)

def addUser(Request):
    form = UserForm(Request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    my_context = {'form' : form}
    return render(Request, 'backend/add_user.html', my_context)

def test1(Request):
    return render(
        Request, 
        'backend/test1.html', 
        context={
            'text' : 'baba', 
            'num' : 1888999, 
            'list': ['ciao', 'paperino', 28765, 3777],
            'auth': None
            })

def test2(Request):
    my_context = {
        'nlist' : [17, 12, 14, 99]
    }
    return render(Request, 'backend/test2.html', my_context)