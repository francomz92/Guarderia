from django.urls import path
from .views import *

urlpatterns = [
    path('registro-proveedor/',
         CrearProveedor.as_view(),
         name='crear_proveedor'),
    path('proveedores/', ListarProveedor.as_view(), name='lista_proveedores'),
    path('editar-proveedor/<pk>/', ModificarProveedor.as_view(), name='editar_proveedor'),
    path('registro-compra/', CrearCompra.as_view(), name='crear_compra'),
    path('compras/', ListarCompra.as_view(), name='lista_compras'),
    path('editar-compra/<pk>/',
         ModificarCompra.as_view(),
         name='editar_compra'),
]