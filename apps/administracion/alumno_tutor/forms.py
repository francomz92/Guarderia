from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django import forms
from django.forms import widgets
from .models import *


class AlumnoForms(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'fecha_nacimiento':
            widgets.DateInput(attrs={
                'type': 'date',
                'min': timezone.now() + relativedelta(years=-100),
                'max': timezone.now() + relativedelta(years=-3, month=6)
            }),
        }


class AsistenciaSelect(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = 'mes',
        widgets = {'mes': widgets.Select(attrs={'id': 'select_mes'})}
