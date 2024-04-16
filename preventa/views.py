from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Preventa


# Create your views here.
def redirect_to_preventa(request):
    return render(request, 'home.html', {})


def addInfo(request):
    return render(request, 'addInfo.html', {})


def ingresar_proyecto(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        proyecto = request.POST.get('proyecto')
        solicitante = request.POST.get('solicitante')
        fecha = request.POST.get('fecha')
        correlativo = request.POST.get('correlativo')
        
        proyecto_nuevo = Preventa(
            cliente=cliente,
            proyecto=proyecto,
            solicitante=solicitante,
            fecha=fecha,
            correlativo=correlativo
        )
        proyecto_nuevo.save()
        
        return redirect('preventa')

    return render(request, 'preventa')
