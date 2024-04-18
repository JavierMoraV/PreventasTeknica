from django.shortcuts import render
from .forms import ClienteForm, PreventaForm
from .models import Preventa

# Create your views here.
def redirect_to_preventa(request):
    return render(request, 'home.html', {})


def addInfo(request, preventa_id):
    preventa = Preventa.objects.get(pk=preventa_id)
    print(preventa)
    return render(request, 'addInfo.html', {'preventa': preventa})


def home_preventa(request):
    if request.method == 'POST':
        if 'submit_cliente' in request.POST: 
            form_cliente = ClienteForm(request.POST)
            if form_cliente.is_valid():
                form_cliente.save()
        elif 'submit_preventa' in request.POST:
            form_preventa = PreventaForm(request.POST)
            if form_preventa.is_valid():
                form_preventa.save()
    load_preventas = Preventa.objects.all()
    form_cliente = ClienteForm()
    form_preventa = PreventaForm()
    return render(request, 'home.html', {'ClienteForm': form_cliente, 
                                         'PreventaForm': form_preventa,
                                         'LoadPreventas': load_preventas})
   


