from django.db import models
from django.forms.models import model_to_dict


class Taller(models.Model):
    nombre = models.CharField(verbose_name='Nombre del taller', max_length=50)
    fecha = models.DateField(verbose_name='Fecha de realización')
    tema = models.CharField(verbose_name='Tematica abordada', max_length=50)
    alumnos = models.PositiveSmallIntegerField(verbose_name='Niños/as')
    familias = models.PositiveSmallIntegerField(verbose_name='Familias')
    asistieron = models.PositiveSmallIntegerField(
        verbose_name='Cantidad de asistentes')
    formdor = models.CharField(verbose_name='Quién brindo la capacitación.?',
                               max_length=50)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'