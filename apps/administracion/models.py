from django.db import models
from django.forms.models import model_to_dict


class ORG(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    directora = models.CharField(verbose_name='Director/a', max_length=50)
    direccion = models.CharField(verbose_name='Direccion', max_length=50)
    telefono = models.IntegerField(verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Correo electrónico', max_length=50)
    fecha_alta = models.DateField(max_length=25)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'ORG'
        verbose_name_plural = 'ORGs'