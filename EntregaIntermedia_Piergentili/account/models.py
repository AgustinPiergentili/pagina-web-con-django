from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registro (User.Model):
    ID_Usuario = models.AutoField(primary_key = True)
    Nombre_Usuario = models.CharField(max_length= 15, blank= False, null= False)
    Contraseña  = models.CharField(max_length= 20, blank= False, null= False)
