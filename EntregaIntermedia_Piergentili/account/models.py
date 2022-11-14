from django.db import models
# Create your models here.

class CrearPost (models.Model):
    Nombre = models.CharField(max_length=40)
    Post  = models.CharField(max_length=240)
