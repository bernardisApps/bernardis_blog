from django.shortcuts import render, redirect
from .forms import RegistrationForm, loginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from publicaciones.models import Publicacion

def registro(request):
    if request.user.is_authenticated:
         return redirect(reverse('main'))
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('login'))
        else:
            form = RegistrationForm()
        return render(request, 'registro.html', {'form':form})

def login_form(request):

    if request.user.is_authenticated:
         return redirect(reverse('main'))
    else:
        form = loginForm()

        if request.method == 'POST':

            form = loginForm(request.POST)
            if form.is_valid():
                user = authenticate(username = request.POST['username'], password = request.POST['password'])
                if user is not None:
                    login(request, user)
                    return redirect(reverse('main'))
                else:
                    messages.info(request, 'No existe')

        return render(request, 'login.html',{'form':form})

@login_required
def main(request):
    if request.method == 'POST':
         usuario = request.user
         contenido = request.POST['contenido']
         publi = Publicacion(usuario = usuario, contenido = contenido)
         publi.save()
         return redirect(reverse('main'))
    
    user = request.user
    publicaciones = Publicacion.objects.all().reverse()
    context = {'user': user, 'publicaciones' : publicaciones}
    return render(request, 'main.html', context)

def logout_view(request):

            logout(request)
            return redirect(reverse('main'))


