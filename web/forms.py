from django.conf import settings
from django import forms
from web.models import Entidad, Enlace, Sesion


class EntidadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200,
                             help_text="Por favor introduzca el nombre de la Entidad")

    class Meta:
        model = Entidad
        fields = {'nombre'}


class EnlaceForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200)
    apellido_pat = forms.CharField(max_length=200)
    apellido_mat = forms.CharField(max_length=200)
    cargo = forms.CharField(max_length=200)

    class Meta:
        model = Enlace
        fields = ['nombre', 'apellido_pat', 'apellido_mat', 'cargo']


class SesionForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200)
    fecha = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,
                                widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))
    acuerdo = forms.CharField(widget=forms.Textarea)
    fecha_prox = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all())
    enlaces = forms.ModelMultipleChoiceField(queryset=Enlace.objects.all())

    class Meta:
        model = Sesion
        fields = ['nombre', 'fecha', 'acuerdo', 'fecha_prox']
