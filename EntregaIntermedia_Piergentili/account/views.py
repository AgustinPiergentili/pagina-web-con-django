from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from account.models import *
from .forms import CrearReseñaForm,CategoriaForm,AutorForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def index(request):
    return render(request, 'account/index.html')


def CrearReseña(request):


    if request.method == 'POST':

        formulario = CrearReseñaForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            reseña = Reseña(nombre=formulario_limpio['nombre'], reseña=formulario_limpio['reseña']) 
            
            reseña.save()

            return render (request, 'account/index.html')
    else:
        formulario = CrearReseñaForm()

    return render(request,'account/crearreseña.html',{'formulario':formulario})


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



def buscar_reseña(request):

    if request.GET.get('resena', False):
        resena = request.GET['resena']
        resenas = Reseña.objects.filter(nombre__icontains=resena)

        return render(request,'account/buscar_resena.html', {'resenas':resenas})
    else:
        respuesta = 'No hay datos'
    return render(request, 'account/buscar_resena.html', {'respuesta':respuesta})



def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request,'account/index.html',{'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request,'account/index.html',{'mensaje':'Error, datos incorrectos'})
        
        else:

                return render(request,'account/index.html',{'mensaje':'Error, formulario erroneo'})

    form = AuthenticationForm()

    return render(request,'account/login.html', {'form':form})



def register(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,'account/index.html', {'mensaje':'Usuario Creado'})

    else:
        form = UserCreationForm()

    return render(request, 'account/registro.html', {'form':form})
    



class ReseñaList(ListView):

    model = Reseña
    template_name = "account/reseña_list.html"

class ReseñaDetail(DetailView):
    model = Reseña
    template_name = 'account/reseña_detalle.html'


class ReseñaDelete(DeleteView):
    model = Reseña 
    success_url = '/reseña_list'

class ReseñaUpdate(UpdateView):

    model = Reseña
    success_url = '/reseña_list'
    fields = ["nombre","reseña"]