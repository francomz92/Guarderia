from django.db import models
from django.forms.models import model_to_dict

MESES = [
    ('enero', 'Enero'),
    ('febrero', 'Febrero'),
    ('marzo', 'Marzo'),
    ('abril', 'Abril'),
    ('mayo', 'Mayo'),
    ('junio', 'Junio'),
    ('julio', 'Julio'),
    ('agosto', 'Agosto'),
    ('septiembre', 'Septiembre'),
    ('octubre', 'Octubre'),
    ('noviembre', 'Noviembre'),
    ('diciembre', 'Diciembre'),
]


class Tutor(models.Model):
    nombre = models.CharField(verbose_name='Nombre',
                              max_length=25,
                              db_index=True)
    apellido = models.CharField(verbose_name='Apellido',
                                max_length=25,
                                db_index=True)
    dni = models.PositiveIntegerField(verbose_name='DNI',
                                      unique=True,
                                      db_index=True)
    telefono = models.IntegerField(verbose_name='Teléfono')
    direccion = models.CharField(verbose_name='Dirección', max_length=50)
    foto = models.FileField(verbose_name='Foto del documento',
                            upload_to='tutores',
                            null=True,
                            blank=True)

    def toJSON(self):
        return model_to_dict(self,
                             fields=[
                                 'id', 'nombre', 'apellido', 'dni', 'telefono',
                                 'direccion'
                             ])

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'


class Alumno(models.Model):
    nombre = models.CharField(verbose_name='Nombre',
                              max_length=25,
                              db_index=True)
    apellido = models.CharField(verbose_name='Apellido',
                                max_length=25,
                                db_index=True)
    dni = models.PositiveIntegerField(verbose_name='DNI',
                                      unique=True,
                                      db_index=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    fecha_alta = models.DateField(verbose_name='Fecha de inscripción',
                                  auto_now_add=True)
    activo = models.BooleanField(verbose_name='Activo.?', default=True)
    if not activo:
        fecha_baja = models.DateField(verbose_name='Fecha de egreso',
                                      auto_now_add=True)
    foto = models.FileField(verbose_name='Foto del documento',
                            upload_to='alumnos/',
                            null=True,
                            blank=True)
    tutor = models.ForeignKey(to=Tutor,
                              verbose_name='Tutor',
                              on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Asistencia(models.Model):
    alumno = models.ForeignKey(to=Alumno,
                               verbose_name='Alumno',
                               on_delete=models.CASCADE)
    mes = models.CharField(verbose_name='Mes', max_length=20, choices=MESES)
    asistio = models.PositiveSmallIntegerField(verbose_name='Asistio')
    falto = models.PositiveSmallIntegerField(verbose_name='No asistio')
    debio_asistir = models.PositiveSmallIntegerField(
        verbose_name='Debio asistir')

    def toJSON(self):
        return model_to_dict(self)

    def __str__(self) -> str:
        return self.alumno.nombre + self.alumno.apellido + '-' + str(
            self.asistio) + 'días'

    class Meta:
        verbose_name = 'Asistencia - Alumno'
        verbose_name_plural = 'Asistencias - Alumnos'
