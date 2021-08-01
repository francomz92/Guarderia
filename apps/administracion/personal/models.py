from django.db import models
from django.forms.models import model_to_dict

ROL = [('Director/a', 'Director/a'), ('Docente', 'Docente'),
       ('Auxiliar', 'Auxiliar'), ('Administrativo', 'Administrativo')]

TURNO = [('Mañana', 'Mañana'), ('Tarde', 'Tarde'),
         ('Jornada Completa', 'Jornada Completa')]


class Personal(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    apellido = models.CharField(verbose_name='Apellido', max_length=50)
    dni = models.PositiveIntegerField(verbose_name='DNI',
                                      unique=True,
                                      db_index=True)
    rol = models.CharField(verbose_name='Rol', choices=ROL, max_length=20)
    jornada = models.CharField(verbose_name='Turno',
                               choices=TURNO,
                               max_length=20)
    observaciones = models.CharField(verbose_name='Observaciones',
                                     max_length=500)
    titulo = models.CharField(verbose_name='Título', max_length=50)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.nombre + self.apellido

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'


class Asistencia(models.Model):
    persona = models.ForeignKey(to=Personal,
                                verbose_name='Empleado',
                                on_delete=models.CASCADE)
    asistio = models.PositiveSmallIntegerField(verbose_name='Asistio')
    falto = models.PositiveSmallIntegerField(verbose_name='No asistio')
    total_debido = models.PositiveSmallIntegerField(
        verbose_name='Debio asistir')

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.persona.nombre + self.persona.apellido + '-' + str(
            self.asistio) + 'días'

    class Meta:
        verbose_name = 'Asistencia - Personal'
        verbose_name_plural = 'Asistencias - Personal'
