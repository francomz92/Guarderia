import json
from datetime import datetime
from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import ALL_FIELDS
from .models import *
from .forms import AlumnoForms, AsistenciaSelect

# ------------------ Tutores ------------------


class CrearTutor(CreateView):
    model = Tutor
    template_name = 'crear_tutor.html'
    success_url = reverse_lazy('administracion:lista_tutores')
    fields = ALL_FIELDS

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nuevo Tutor'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


@method_decorator(csrf_exempt, name='dispatch')
class ListarTutores(ListView):
    model = Tutor
    template_name = 'lista_tutores.html'
    context_object_name = 'tutores'
    queryset = Tutor.objects.all()

    @never_cache
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Json = []
            try:
                for registro in self.get_queryset():
                    # Creación de  cada objeto
                    data = registro.toJSON()
                    if registro.foto:
                        data['foto'] = registro.foto.url
                    else:
                        data['foto'] = '-'
                    data['accion'] = ''
                    # Agregando a la lista
                    Json.append(data)
            except Exception as err:
                print(err)
            return JsonResponse(Json, safe=False)
        else:
            contex_data = {'title': 'Tutores'}
            return render(request, self.template_name, contex_data)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarTutor(UpdateView):
    model = Tutor
    template_name = 'modificar_tutor.html'
    success_url = reverse_lazy('administracion:lista_tutores')
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(Tutor, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Tutor'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data


# ------------------ Alumnos ------------------


class CrearAlumno(CreateView):
    model = Alumno
    form_class = AlumnoForms
    template_name = 'crear_alumno.html'
    success_url = reverse_lazy('administracion:lista_alumnos')

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nuevo Alumno'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


class DetalleAlumno(DetailView):
    model = Alumno
    template_name = 'detalle_alumno.html'
    context_object_name = 'alumno'

    def get_object(self):
        return get_object_or_404(Alumno, pk=self.kwargs['pk'])


@method_decorator(csrf_exempt, name='dispatch')
class ListarAlumnos(ListView):
    model = Alumno
    template_name = 'lista_alumnos.html'
    context_object_name = 'alumnos'
    queryset = Alumno.objects.all()

    @never_cache
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Json = []
            try:
                for registro in self.get_queryset():
                    # Creación de cada objeto
                    data = {
                        'id': registro.id,
                        'nombre': registro.nombre,
                        'apellido': registro.apellido,
                        'dni': registro.dni,
                        'fecha_nacimiento': datetime.strftime(registro.fecha_nacimiento, '%d %b de %Y'),
                        'activo': registro.activo
                    }
                    if registro.foto:
                        data['foto'] = registro.foto.url
                    else:
                        data['foto'] = '-'
                    data['accion'] = ''
                    # Agregando a la lista
                    Json.append(data)
                return JsonResponse(Json, safe=False)
            except Exception as err:
                print(err)
        else:
            contex_data = {'title': 'Alumnos'}
            return render(request, self.template_name, contex_data)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarAlumno(UpdateView):
    model = Alumno
    template_name = 'modificar_alumno.html'
    success_url = reverse_lazy('administracion:lista_alumnos')
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(Alumno, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Alumno'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data

# ------------------ Asistencias ------------------


class CrearAsistencia(CreateView):
    model = Asistencia
    template_name = 'crear_asistencia.html'
    success_url = reverse_lazy('administracion:lista_asistencias')
    fields = ALL_FIELDS

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nueva Asistencia'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


@method_decorator(csrf_exempt, name='dispatch')
class ListarAsistencias(ListView):
    model = Asistencia
    template_name = 'lista_asistencias.html'
    context_object_name = 'asistencias'
    queryset = Asistencia.objects.all()

    @never_cache
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Json = []
            try:
                for registro in self.get_queryset():
                    # Creación de cada objeto
                    data = {
                        'id': registro.id,
                        'nombre': registro.alumno.nombre,
                        'apellido': registro.alumno.apellido,
                        'dni': registro.alumno.dni,
                        'asistio': registro.asistio,
                        'falto': registro.falto,
                        'debio_asistir': registro.debio_asistir
                    }
                    if registro.foto:
                        data['foto'] = registro.foto.url
                    else:
                        data['foto'] = '-'
                    data['accion'] = ''
                    # Agregando a la lista
                    Json.append(data)
                return JsonResponse(Json, safe=False)
            except Exception as err:
                print(err)
        else:
            contex_data = {
                'title': 'Asistencias',
                'mes': AsistenciaSelect
            }
            return render(request, self.template_name, contex_data)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarAsistencia(UpdateView):
    model = Asistencia
    template_name = 'modificar_asistencia.html'
    success_url = reverse_lazy('administracion:lista_asistncias')
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(Asistencia, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Asistencia'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data