from django.urls import path
from django.urls.conf import include
from .views import *

app_name = 'administracion'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('alumno-tutor/', include('apps.administracion.alumno_tutor.urls')),
    path('gastos/', include('apps.administracion.gastos.urls')),
    path('personal/', include('apps.administracion.personal.urls')),
    path('talleres-actividades/',
         include('apps.administracion.talleres_actividades.urls')),
]
