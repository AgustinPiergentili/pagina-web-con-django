from django.db import models
# Create your models here.

class Post (models.Model):
    Nombre = models.CharField(max_length=40)
    Post  = models.CharField(max_length=240)

    def __str__(self) -> str:
        return f"Nombre: {self.Nombre} - POST: {self.Post}"
    

class Categoria (models.Model):
    nombre = models.CharField('nombre categoria',max_length=50,null=False)
    estado = models.BooleanField('activa / no activa',default=True)
    fecha_creacion = models.DateField('fecha de creacion',auto_now=False,auto_now_add=True)


class Autor(models.Model):
    nombre = models.CharField('Nombre autor',max_length=40)
    apellido= models.CharField('Apellido Autor', max_length=255)
    estado = models.BooleanField('activo / inactivo', default= True)

