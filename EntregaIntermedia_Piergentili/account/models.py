from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.

class Reseña (models.Model):
    nombre = models.CharField(max_length=40)
    reseña  = models.CharField(max_length=240)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Reseña: {self.reseña}"
    class Reseña(LoginRequiredMixin):
        pass

class Categoria (models.Model):
    genero = models.CharField(max_length=50,default="Some String")

    def __str__(self) -> str:
        return f"Genero: {self.genero}"

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"


