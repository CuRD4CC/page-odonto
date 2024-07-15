from django import forms
from .models import Experiencia

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['titulo', 'imagen', 'texto']
