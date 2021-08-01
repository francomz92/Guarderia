import json
from django.forms.models import ALL_FIELDS
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *


class CrearPersonal(CreateView):
    model = Personal
    template_name = 'crear_personal.html'
    success_url = reverse_lazy('administracion:lista_personal')
    fields = ALL_FIELDS

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nuevo Empleado'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


class DetallePersonal(DetailView):
    model = Personal
    template_name = 'detalle_personal.html'

    def get_object(self):
        return get_object_or_404(Personal, pk=self.kwargs['pk'])

@method_decorator(csrf_exempt, name='dispatch')
class ListarPersonal(ListView):
    model = Personal
    template_name = 'lista_personal.html'
    context_object_name = 'personal'
    queryset = Personal.objects.all()

    @never_cache
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Json = []
            try:
                for registro in self.get_queryset():
                    # Creación de cada objeto
                    data = {
                        'id': registro.id,
                        'fecha': registro.nombre,
                        'factura': registro.apellido,
                        'proveedor': registro.dni,
                        'cuit': registro.rol,
                        'detalle': registro.titulo,
                        'cantidad': registro.jornada,
                        'accion': ''
                    }
                    # Agregando a la lista
                    Json.append(data)
                return JsonResponse(Json, safe=False)
            except Exception as err:
                print(err)
        else:
            contex_data = {
                'title': 'Personal',
            }
            return render(request, self.template_name, contex_data)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarPersonal(UpdateView):
    model = Personal
    template_name = 'modificar_personal.html'
    success_url = 'administracion:lista_personal'
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(Personal, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Empleado'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data
