from django.shortcuts import render, redirect
from .forms import ProyectoForm


# Create your views here.
def redirect_to_preventa(request):
    return render(request, 'home.html', {})


def addInfo(request):
    return render(request, 'addInfo.html', {})


# views.py

def ingresar_proyecto(request):
    print('probando')
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  # Aquí debes especificar la ruta a la que quieres redirigir después de guardar el formulario
    else:
        form = ProyectoForm()
    
    return render(request, 'home.html', {'form': form})
