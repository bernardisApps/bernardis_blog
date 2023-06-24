from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "El ususario %s ha publicado en %s"%(self.usuario,self.fecha_publicacion)
