import json
from django.forms.models import ALL_FIELDS
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .models import *

# ------------------ Proveedor ------------------


class CrearProveedor(CreateView):
    model = Proveedor
    template_name = 'crear_proveedor.html'
    success_url = reverse_lazy('administracion:lista_proveedores')
    fields = ALL_FIELDS

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nuevo Proveedor'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


@method_decorator(csrf_exempt, name='dispatch')
class ListarProveedor(ListView):
    model = Proveedor
    template_name = 'listar_proveedor.html'
    context_object_name = 'proveedores'
    queryset = Proveedor.objects.all()
    
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
                        'cuit': registro.cuit,
                        'direccion': registro.direccion,
                        'telefono': registro.telefono,
                        'accion': ''
                    }
                    # Agregando a la lista
                    Json.append(data)
                return JsonResponse(Json, safe=False)
            except Exception as err:
                print(err)
        else:
            contex_data = {
                'title': 'Proveedores',
            }
            return render(request, self.template_name, contex_data)

    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarProveedor(UpdateView):
    model = Proveedor
    template_name = 'modificar_proveedor.html'
    success_url = reverse_lazy('administracion:lista_proveedores')
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Proveedor'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data
    
    
# ------------------ Compra ------------------


class CrearCompra(CreateView):
    model = Compra
    template_name = 'crear_compra.html'
    success_url = reverse_lazy('administracion:lista_compras')
    fields = ALL_FIELDS

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Nueva Compra'
        contex_data[
            'msj'] = 'Complete los datos requeridos para un nuevo registro.'
        return contex_data


@method_decorator(csrf_exempt, name='dispatch')
class ListarCompra(ListView):
    model = Compra
    template_name = 'listar_compra.html'
    context_object_name = 'compras'
    
    @never_cache
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            Json = []
            try:
                for registro in self.get_queryset():
                    # Creación de cada objeto
                    data = {
                        'id': registro.id,
                        'fecha': registro.fecha,
                        'factura': registro.factura,
                        'proveedor': registro.proveedor.nombre,
                        'cuit': registro.proveedor.cuit,
                        'detalle': registro.detalle,
                        'cantidad': registro.cantidad,
                        'monto': registro.monto,
                        'accion': ''
                    }
                    # Agregando a la lista
                    Json.append(data)
                return JsonResponse(Json, safe=False)
            except Exception as err:
                print(err)
        else:
            contex_data = {
                'title': 'Compras',
            }
            return render(request, self.template_name, contex_data)
        
    def post(self, request, *args, **kwargs):
        request_data = json.loads(request.body)
        if request_data['action'] == 'delete':
            get_object_or_404(self.model, pk=request_data['id']).delete()
        return self.get(request, *args, **kwargs)


class ModificarCompra(UpdateView):
    model = Compra
    template_name = 'modificar_compra.html'
    success_url = reverse_lazy('administracion:lista_compras')
    fields = ALL_FIELDS

    def get_object(self):
        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = 'Editar Proveedor'
        contex_data['msj'] = 'Actualice la infomación que necesite.'
        return contex_data

