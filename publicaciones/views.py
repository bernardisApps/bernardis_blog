from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Publicacion

# Create your views here.


def borrar_publi(request,id_publi):
    publi = Publicacion.objects.get(id = id_publi)
    publi.delete()
    return redirect(reverse('main'))

@login_required
def nueva_publi(request):

    if request.method == 'POST':
        usuario = request.user
        contenido = request.POST['contenido']
        publi = Publicacion(usuario = usuario, contenido = contenido)
        publi.save()
        return redirect(reverse('main'))
