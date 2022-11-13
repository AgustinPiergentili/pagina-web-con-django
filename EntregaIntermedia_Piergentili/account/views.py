from django.shortcuts import render
from django.http import HttpResponse
from account.forms import CrearUsuario
# Create your views here.

def index(request):
    return render(request, 'account/templates/account/index.html')

def mostrar_registro(request):
    return render(request,'account/templates/account/registro.html')

def FormularioRegistro(request):

    if request.method == 'POST':
        user = User(Usuario=request.POST['nombre'],Contrasenia=request.POST['contrasenia']) 
        user.save()

        return render (request, 'account/templates/account/index.html')
    else:
        formulario = CrearUsuario()

    return render(request,'account/templates/account/formularioregistro.html',{'formulario':formulario})