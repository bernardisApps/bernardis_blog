from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Publicacion

# Create your views here.


def borrar_publi(request,id_publi):
    publi = Publicacion.objects.get(id = id_publi)
    publi.delete()
    return redirect(reverse('main'))
