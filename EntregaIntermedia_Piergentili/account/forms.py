from django import forms

class CrearPostForm(forms.Form):
    Nombre = forms.CharField(max_length=40)
    Post = forms.CharField(max_length=240)
