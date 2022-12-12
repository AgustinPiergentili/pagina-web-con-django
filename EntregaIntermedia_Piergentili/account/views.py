from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# import form & model
from account.models import *
from .forms import CrearReseñaForm,CategoriaForm,AutorForm,SignUpform,UserEditForm,CrearComentarioForm

#Auth
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Redireccion
from django.urls import reverse_lazy

###------------------------------------------------------------------###

# Create your views here.

def index(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, 'account/index.html',{"avatares":avatares})



@login_required
def CrearReseña(request):


    if request.method == 'POST':

        formulario = CrearReseñaForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            reseña = Reseña(nombre=formulario_limpio['nombre'], reseña=formulario_limpio['reseña'],titulo=formulario_limpio['titulo'],
            genero=formulario_limpio['genero']) #,imagen=formulario_limpio['imagen']) 
            

            reseña.save()

            return render (request, 'account/index.html')
    else:
        formulario = CrearReseñaForm()

    return render(request,'account/crearreseña.html',{'formulario':formulario})



@login_required
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



@login_required
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



@login_required
def buscar_reseña(request):

    if request.GET.get('resena', False):
        resena = request.GET['resena']
        resenas = Reseña.objects.filter(nombre__icontains=resena)

        return render(request,'account/buscar_resena.html', {'resenas':resenas})
    else:
        respuesta = 'No hay datos'
    return render(request, 'account/buscar_resena.html', {'respuesta':respuesta})



@login_required
def editar_user(request):

    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request,'account/index.html')
    
    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
        })
    return render(request,'account/admin_update.html',{
        'form': usuario_form,
        'usuario': usuario
    })



@login_required
def AgregarAvatar(request):
    if request.method == 'POST':

        miformulario = Avatar(request.POST, request.FILES)

        if miformulario.is_valid:

            u=User.objects.get(username=request.user)

            avatar = Avatar(user=u, imagen=miformulario.cleaned_data['imagen'])

            avatar.save()

            return render(request, 'account/index.html')

    else:
        miformulario= Avatar()
    
    return render(request, "account/agregaravatar.html", {'miformulario':miformulario})


@login_required
def CrearComentario(request):


    if request.method == 'POST':

        formulario = CrearComentarioForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            comentario = Comentario(nombre=formulario_limpio['nombre'], comentario=formulario_limpio['comentario']) 
            

            comentario.save()

            return render (request, 'account/crear_ comentario.html')
    else:
        formulario = CrearComentarioForm()

    return render(request,'account/crear_comentario.html',{'formulario':formulario})



#####VISTAS BASADAS EN CLASES!!#####



class ReseñaList(LoginRequiredMixin, ListView):

    model = Reseña
    template_name = "account/reseña_list.html"


class ReseñaDetail(LoginRequiredMixin,DetailView):
    model = Reseña
    template_name = 'account/reseña_detalle.html'


class ReseñaDelete(LoginRequiredMixin,DeleteView):
    model = Reseña 
    success_url = '/reseña_list'


class ReseñaUpdate(LoginRequiredMixin,UpdateView):

    model = Reseña
    success_url = '/reseña_list'
    fields = [
        "nombre",
        "reseña"
        ]


class SignUpView(CreateView):

    form_class = SignUpform
    success_url = reverse_lazy('index')
    template_name = 'account/registro.html'


class AdminLoginView(LoginView):
    template_name = 'account/login.html'


class AdminLogoutView(LogoutView):
    template_name = 'account/index.html'  
