from django import forms
from web.models import Entidad, Enlace


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
        fields = {'cargo', 'nombre', 'apellido_pat', 'apellido_mat'}