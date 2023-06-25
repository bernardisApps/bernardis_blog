from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def ver_perfil(request, username):
    context = {'username':username}
    return render(request, 'perfil.html', context)
