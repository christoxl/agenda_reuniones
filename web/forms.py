from django import forms
from web.models import Entidad


class EntidadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200,
                             help_text="Por favor introduzca el nombre de la Entidad")

    class Meta:
        model = Entidad
        fields = {'nombre'}
