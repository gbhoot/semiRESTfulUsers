from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import datetime

# Create your views here.
def root(request):
    return redirect('/users/')

def index(request):
    data = {
        'users' :   User.objects.all()
    }
    return render(request, 'index.html', data)

def show(request, id):
    data = {
        'user'  :   User.objects.get(id=id)
    }
    return render(request, 'show.html', data)

def new(request):
    return render(request, 'new.html')

def add(request):
    errors = User.objects.basic_validator(request.POST)
    currentTime = datetime.datetime.now()

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/users/new/')
    
    newUser = User.objects.create(first_name=request.POST['fName'], last_name=request.POST['lName'], 
        email=request.POST['email'], created_at=currentTime, updated_at=currentTime)
    print(newUser)
    print(newUser.id)
    
    return redirect('/users/'+str(newUser.id))

def edit(request, id):
    data = {
        'user'  :   User.objects.get(id=id)
    }

    return render(request, 'edit.html', data)

def update(request, id):
    user = User.objects.get(id=id)

    errors = User.objects.basic_validator(request.POST, id, True)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/users/'+str(id)+'/edit/')
    
    user.first_name = request.POST['fName']
    user.last_name = request.POST['lName']
    user.email = request.POST['email']
    user.updated_at = datetime.datetime.now()
    user.save()

    return redirect('/users/'+str(id))

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect('/')
