from django.urls import path
from .views import index, mostrar_registro,FormularioRegistro

urlpatterns = [
    path('', index),
    path('mostrar_registro/', mostrar_registro,name='Registro'),
    path('formulario_registro/', FormularioRegistro,name='FormularioRegistro')
]
