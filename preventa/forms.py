from django import forms
from .models import Cliente, Preventa, Item

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']
        

class PreventaForm(forms.ModelForm):
    class Meta:
        model = Preventa
        fields = ['id_cliente', 'nombre_proyecto', 'nombre_solicitante','nombre_vertical', 'fecha', 'correlativo']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre_item', 'detalle_item', 'valor_unitario']
        
