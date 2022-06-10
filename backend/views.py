from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from os import listdir
from .models import User, File
from backend.utils.db import validate_user
from django.middleware.csrf import get_token

# Create your views here.
def index(Request):
    print(Request.session['authenticated'])
    return render(Request, 'backend/index.html')

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
        form = FileForm()
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
    if 'search_button' in Request.GET:
        q = Request.GET['q']
        files = File.objects.filter(name__contains=str(q)) 
    else:
        files = "There are no files with that name."
    my_context = {'nlist' : [17, 12, 14, 99], 'myfile' : files}
    return render(Request, 'backend/test2.html', my_context)

def log_in(Request):
    submit = [None,None]
    session = Request.session
    session.__setitem__('authenticated', False)
    session.__setitem__('name', None)

    if 'submit_button' in Request.POST:
        submit = [Request.POST['username'], Request.POST['password']]

        if validate_user(submit[0], submit[1]):
            user = submit[0]
            session.__setitem__('authenticated', True)
            session.__setitem__('name', submit[0])
            print(
                session['authenticated'],
                session['name'])
            return render(Request, 'backend/index.html')
        else:
            return render(Request, 'backend/log_in.html')
    else:
            

        return render(Request, 'backend/log_in.html')

def log_out(Request):
    session = Request.session
    session.__setitem__('authenticated', False)
    print(session['authenticated'])
    return render(Request, 'backend/log_in.html')



# def log_in(Request):
#     return render(Request, 'backend/log_in.html')