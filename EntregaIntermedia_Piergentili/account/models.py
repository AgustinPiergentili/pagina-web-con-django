from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your models here.

class Reseña (models.Model):
    nombre = models.CharField(max_length=40)
    titulo = models.CharField(max_length=50,default='some_value')
    genero = models.CharField(max_length=30,default='some_value')
    reseña  = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Titulo: {self.titulo} - Genero: {self.genero}"



class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.CharField(max_length=240)



class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='media/images/', null=True, blank=True)

