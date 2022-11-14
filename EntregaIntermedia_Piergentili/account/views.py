from .forms import CrearPostForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import CrearPost

# Create your views here.

def index(request):
    return render(request, 'account/templates/account/index.html')


def CrearPost(request):


    if request.method == 'POST':

        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Post(Nombre=formulario_limpio['Nombre'], Post=formulario_limpio['Post']) 
            
            post.save()

            return render (request, 'account/templates/account/index.html')
    else:
        formulario = CrearPostForm()

    return render(request,'account/templates/account/crearpost.html',{'formulario':formulario})

def buscar_post(request):

    if request.GET.get('post', False):
        post = request.GET['post']
        nombre = nombre.objects.filter(post__icontains=post)

        return render(request,'account/templates/account/buscar_post.html', {'nombre':nombre})
    else:
        respuesta = 'No hay datos'
    return render(request, 'account/templates/account/buscar_post.html', {'respuesta':respuesta})