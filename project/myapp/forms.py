from django import forms
from .models import Estudiante, Docente

## STEP 2.5 ##

class docenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'email', 'especialidad']
        
class estudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']