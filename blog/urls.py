"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login.views import registro,login_form,main, logout_view
from publicaciones.views import borrar_publi, nueva_publi
from perfiles.views import ver_perfil

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('registro/',registro, name='registro'),
    path('accounts/login/',login_form,name='login'),
    path('logout/',logout_view, name='logout'),
    path('borrar/<int:id_publi>', borrar_publi, name='borrar_publi' ),
    path('nueva/', nueva_publi, name='nueva_publi'),
    path('perfil/<username>', ver_perfil, name='perfil')
]
