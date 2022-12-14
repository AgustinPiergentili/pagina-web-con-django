from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearReseñaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    titulo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=30)
    reseña = forms.CharField(max_length=240)


class CrearComentarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    comentario = forms.CharField(max_length=240)




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

