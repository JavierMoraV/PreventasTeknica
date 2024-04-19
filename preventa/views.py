from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ClienteForm, PreventaForm, ItemForm
from .models import Preventa

# Create your views here.
def redirect_to_preventa(request):
    return render(request, 'home.html', {})


def addInfo(request, preventa_id):
    preventa = Preventa.objects.get(pk=preventa_id)
    print(preventa)
    return render(request, 'addInfo.html', {'preventa': preventa})


@login_required
def home_preventa(request):
    if request.method == 'POST':
        if 'submit_cliente' in request.POST: 
            form_cliente = ClienteForm(request.POST)
            if form_cliente.is_valid():
                form_cliente.save(usuario_tecnica=request.user)
        elif 'submit_preventa' in request.POST:
            form_preventa = PreventaForm(request.POST)
            if form_preventa.is_valid():
                preventa = form_preventa.save(commit=False)
                preventa.usuario_teknica = request.user
                preventa.save()
        elif 'submit_item' in request.POST:
            form_item = ItemForm(request.POST)
            if form_item.is_valid():
                form_item.save()
    load_preventas = Preventa.objects.all()
    form_cliente = ClienteForm()
    form_preventa = PreventaForm()
    form_item = ItemForm()
    return render(request, 'home.html', {'ClienteForm': form_cliente, 
                                         'PreventaForm': form_preventa,
                                         'LoadPreventas': load_preventas,
                                         'ItemForm': form_item})
   


