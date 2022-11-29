from django import forms

class CrearReseñaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    reseña = forms.CharField(max_length=240)

class CategoriaForm (forms.Form):
    genero = forms.CharField(max_length=50)


class AutorForm (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido= forms.CharField()
    edad = forms.IntegerField()


