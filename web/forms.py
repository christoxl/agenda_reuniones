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
        fields = {'cargo', 'nombre', 'apellido_pat', 'apellido_mat'}


class SesionForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200)
    fecha = forms.DateTimeField()
    acuerdo = forms.CharField(widget=forms.Textarea)
    fecha_prox = forms.DateTimeField()
    # entidad = forms.ModelChoiceField(queryset=Entidad.objects.all())
    # enlaces = forms.ModelChoiceField(queryset=Enlace.objects.all())

    class Meta:
        model = Sesion
        fields = {'nombre', 'fecha', 'acuerdo', 'fecha_prox'}
