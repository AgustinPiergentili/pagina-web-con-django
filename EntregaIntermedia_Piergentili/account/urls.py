from django.urls import path
from .views import index,CrearPost,buscar_post

urlpatterns = [
    path('', index,name='index'),
    path('crear_post/', CrearPost,name='CrearPost'),
    path('buscar_post/', buscar_post,name='Buscar Post'),
]
