from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *



def userPage(request):
    drvo = Drvo.objects.all()
    stolica = Stolica.objects.all()
    return render(request, 'stolica/user.html', {'stolica': stolica, 'drvo': drvo})

def user(request):
    user = User.objects.all()
    total_users = user.count()
    brojac = 0
    for u in User.objects.all():
        if '@gmail.com' in u.email:
            brojac = brojac+1
    email = brojac
    return render(request, 'gvozdje/user.html', {'user': user, 'total_users':total_users, 'email':email})