from django.shortcuts import render
from .forms import estudianteForm, docenteForm
# Create your views here.
## STEP 3 ##
def registrar_Estudiante(request):
    form = estudianteForm()
    if request.method == 'POST':
        form = estudianteForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registroEstudiante.html', {'form': form})