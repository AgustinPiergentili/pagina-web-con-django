from .forms import CrearPostForm
from django.http import HttpResponse
from django.shortcuts import render
from account.models import *

# Create your views here.

def index(request):
    return render(request, 'account/index.html')


def CrearPost(request):


    if request.method == 'POST':

        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Post(Nombre=formulario_limpio['Nombre'], Post=formulario_limpio['Post']) 
            
            post.save()

            return render (request, 'account/index.html')
    else:
        formulario = CrearPostForm()

    return render(request,'account/crearpost.html',{'formulario':formulario})

def buscar_post(request):

    if request.GET.get('post', False):
        post = request.GET['post']
        posts = Post.objects.filter(Nombre__icontains=post)

        return render(request,'account/buscar_post.html', {'posts':posts})
    else:
        respuesta = 'No hay datos'
    return render(request, 'account/buscar_post.html', {'respuesta':respuesta})

