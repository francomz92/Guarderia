from django.views.generic.base import TemplateView
from django.urls import path
from .views import *

urlpatterns = [
    path('registro-tutor/', CrearTutor.as_view(), name='crear_tutor'),
    path('tutores/', ListarTutores.as_view(), name='lista_tutores'),
    path('editar-tutor/<pk>/', ModificarTutor.as_view(), name='editar_tutor'),
    path('registro-alumno/', CrearAlumno.as_view(), name='crear_alumno'),
    path('alumno/<pk>/', DetalleAlumno.as_view(), name='detalle_alumno'),
    path('alumnos/', ListarAlumnos.as_view(), name='lista_alumnos'),
    path('editar-alumno/<pk>/',
         ModificarAlumno.as_view(),
         name='editar_alumno'),
    path('asistencias/', ListarAsistencias.as_view(),
         name='lista_asistencias'),
    path('registro-asistencia/',
         CrearAsistencia.as_view(),
         name='crear_asistencia'),
    path('editar-asistencia/<pk>/',
         ModificarAsistencia.as_view(),
         name='editar_asistencia'),
]
