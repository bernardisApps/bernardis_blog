from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Editar_Perfil
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.

def ver_perfil(request, username):
    usuario = request.user
    if username == request.user.username:
        form = Editar_Perfil(instance=usuario)
        context = {'form':form, 'username':username, 'soyyo' : True}
        if request.method == 'POST':
            form = Editar_Perfil(request.POST,instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('main')
    else:
        usuario = User.objects.get(username=username)
        context = {'usuario':usuario, 'username':username, 'soyyo':False}
    return render(request, 'perfil.html', context)
