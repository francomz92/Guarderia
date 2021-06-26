from django.urls import path
from .views import *

urlpatterns = [
    path('empleados/', ListarPersonal.as_view(), name='lista_personal'),
    path('editar-empleado/<pk>/',
         ModificarPersonal.as_view(),
         name='editar_personal'),
    path('registro-personal/', CrearPersonal.as_view(), name='crear_personal'),
]
