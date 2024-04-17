from django import forms
from .models import Cliente, Preventa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']
        

class PreventaForm(forms.ModelForm):
    class Meta:
        model = Preventa
        fields = ['id_cliente', 'nombre_proyecto', 'nombre_solicitante', 'fecha', 'correlativo']


