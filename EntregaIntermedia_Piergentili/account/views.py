from .forms import CrearPostForm,CategoriaForm,AutorForm
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


def CrearCategoria(request):


    if request.method == 'POST':

        formulario2 = CategoriaForm(request.POST)

        if formulario2.is_valid():

            formulario_limpio = formulario2.cleaned_data

            categoria = Categoria(genero=formulario_limpio['genero']) 
            
            categoria.save()

            return render (request, 'account/index.html')
    else:
        formulario2 = CategoriaForm()

    return render(request,'account/crearcategoria.html',{'formulario2':formulario2})


def CrearAutor(request):


    if request.method == 'POST':

        formulario3 = AutorForm (request.POST)

        if formulario3.is_valid():

            formulario_limpio = formulario3.cleaned_data

            autor = Autor(nombre=formulario_limpio['nombre'],apellido=formulario_limpio['apellido'],edad=formulario_limpio['edad']) 
            
            autor.save()

            return render (request, 'account/index.html')
    else:
        formulario3 = AutorForm()

    return render(request,'account/crearautor.html',{'formulario3':formulario3})


def buscar_post(request):

    if request.GET.get('post', False):
        post = request.GET['post']
        posts = Post.objects.filter(Nombre__icontains=post)

        return render(request,'account/buscar_post.html', {'posts':posts})
    else:
        respuesta = 'No hay datos'
    return render(request, 'account/buscar_post.html', {'respuesta':respuesta})

