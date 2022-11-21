from django.urls import path
from .views import index,CrearPost,CrearCategoria,buscar_post,CrearAutor

urlpatterns = [
    path('', index,name='index'),
    path('crear_post/', CrearPost,name='CrearPost'),
    path('crear_categoria/',CrearCategoria,name='Crear Categoria'),
    path('crear_autor/',CrearAutor,name='Crear Autor'),
    path('buscar_post/', buscar_post,name='Buscar Post'),
]
