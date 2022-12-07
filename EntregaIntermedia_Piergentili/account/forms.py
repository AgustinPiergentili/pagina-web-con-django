from django import forms
from django.contrib.auth.models import User
from .models import Autor
from django.contrib.auth.forms import UserCreationForm

class CrearReseñaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    reseña = forms.CharField(max_length=240)

class CategoriaForm (forms.Form):
    genero = forms.CharField(max_length=50)


class AutorForm (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido= forms.CharField()
    edad = forms.IntegerField()


class SignUpform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k:'' for k in fields}


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k:'' for k in fields}

