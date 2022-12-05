from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index,name='index'),
    path('crear_reseña/', CrearReseña,name='Crear Reseña'),
    path('crear_categoria/', CrearCategoria,name='Crear Categoria'),
    path('crear_autor/', CrearAutor,name='Crear Autor'),
    path('buscar_resena/', buscar_reseña,name='Buscar Reseña'),
    path('reseña_list/', ReseñaList.as_view(),name='List'),
    path('reseña_detail/<pk>', ReseñaDetail.as_view(),name='Detail'),
    path('reseña_confirm_delete/<pk>', ReseñaDelete.as_view(),name='Delete'),
    path('reseña_edit/<pk>', ReseñaUpdate.as_view(),name='Update'),
    path('login/',login_request,name='Login'),
    path('registro/',register,name='Register'),
    path('logout/',LogoutView.as_view(template_name='account/logout.html'),name='Logout'),
]
