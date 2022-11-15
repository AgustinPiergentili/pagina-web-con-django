from django.db import models
# Create your models here.

class Post (models.Model):
    Nombre = models.CharField(max_length=40)
    Post  = models.CharField(max_length=240)

    def __str__(self) -> str:
        return f"Nombre: {self.Nombre} - POST: {self.Post}"