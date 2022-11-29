from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('crear_reseña/', CrearReseña,name='Crear Reseña'),
    path('crear_categoria/', CrearCategoria,name='Crear Categoria'),
    path('crear_autor/', CrearAutor,name='Crear Autor'),
    path('buscar_reseña/', buscar_reseña,name='Buscar Reseña'),
    path('reseña_list/', ReseñaList.as_view(),name='List'),
    path('reseña_detail/<pk>', ReseñaDetail.as_view(),name='Detail'),
    path('reseña_confirm_delete/<pk>', ReseñaDelete.as_view(),name='Delete'),
    path('reseña_edit/<pk>', ReseñaUpdate.as_view(),name='Update'),
]
