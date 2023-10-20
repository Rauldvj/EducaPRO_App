from django import forms
from .models import Estudiante

#CREAMOS EL MODELO EL CUAL REGISTRA Y RETORNA EN FORMATO HTML A NUESTRA VISTA DE ESTUDIANTE
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
