from django.db import models
from django.forms.models import model_to_dict


class Proveedor(models.Model):
    nombre = models.CharField(verbose_name='Nombre del Proveedor',
                              max_length=50)
    cuit = models.PositiveIntegerField(verbose_name='CUIT')
    telefono = models.PositiveIntegerField(verbose_name='Teléfono')
    direccion = models.CharField(verbose_name='Dirección', max_length=50)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.cuit}'

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Compra(models.Model):
    fecha = models.DateField(verbose_name='Fecha de Emción')
    proveedor = models.ForeignKey(to=Proveedor,
                                  verbose_name='Proveedor',
                                  on_delete=models.PROTECT)
    factura = models.CharField(verbose_name='Tipo y N° de Factura',
                               max_length=50)
    detalle = models.CharField(verbose_name='Detalle', max_length=50)
    cantidad = models.PositiveSmallIntegerField(verbose_name='Cantidad')
    monto = models.DecimalField(verbose_name='Monto',
                                decimal_places=2,
                                max_digits=8)

    @classmethod
    def total(cls):
        registros = Compra.objects.all()
        total = 0
        for registro in registros:
            total += registro.monto
        return total

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return f'{self.fecha} - {self.proveedor.factura} - {self.monto}'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class Rendicion(models.Model):
    pass