from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class usuario (models.Model):
    Usuario = models.CharField(max_length=40)
    Contraseña  = models.CharField(max_length=40)
    Email = models.EmailField()