from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Experiencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/')
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
