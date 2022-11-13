from django import forms

class CrearUsuario(forms.Form):
    Usuario = forms.CharField(max_length=40)
    Contrasenia = forms.CharField(max_length=40)
    Email = forms.EmailField(max_length=100)