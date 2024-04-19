from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.nombre
    
class Preventa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100, null=False)
    nombre_solicitante = models.CharField(max_length=100, null=False)
    OPCIONES_ENUM = [
        ('estandar', 'Estandar'),
        ('zona_norte_antofagasta', 'Zona Norte Antofagasta'),
        ('data_center', 'Data Center'),
        ('mineria_y_utilities', 'Mineria y Utilities'),
        ('industrias', 'Industrias'),
        ('telecomunicaciones', 'Telecomunicaciones'),
        ('transporte_y_gobierno', 'Transporte y Gobierno'),
    ]
    nombre_vertical = models.CharField(max_length=50, choices=OPCIONES_ENUM)
    fecha = models.DateField(null=False)
    correlativo = models.IntegerField(null=False)
    usuario_teknica = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre_proyecto

class DetalleIngenieria(models.Model):
    id = models.AutoField(primary_key=True)
    id_preventa = models.ForeignKey(Preventa, on_delete=models.CASCADE, null=False)
    usuario_teknica = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    alcance = models.TextField()
    entregables = models.TextField()
    info_requerida_mandante = models.TextField()
    limitaciones = models.TextField()
    exclusiones = models.TextField()
    plazo_entrega = models.TextField()
    costo = models.IntegerField(null=False)
    firma = models.CharField(max_length=100, null=False)
    subtotal_item = models.IntegerField(null=False)
    subtotal_item_neto = models.IntegerField(null=False)
    total_item_neto = models.IntegerField(null=False)
    total_hh = models.IntegerField(null=False)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_item = models.CharField(max_length=100, null=False)
    detalle_item = models.CharField(max_length=100, null=True)
    valor_unitario = models.IntegerField(null=False)

class ItemDetalle(models.Model):
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    id_detalle_ingenieria = models.ForeignKey(DetalleIngenieria, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(null=False)
    costo_total = models.IntegerField(null=False)
    precio_total = models.IntegerField(null=False)

class HorasHombre(models.Model):
    id = models.AutoField(primary_key=True)
    OPCIONES_ENUM = [
        ('pm', 'Project Manager'),
        ('ie', 'Ingeniero Especialista'),
        ('dp', 'Dibujante Proyectista'),
        ('cd', 'Control Documentos'),
        ('sp', 'Supervisor de Proyecto'),
        ('it', 'Ingeniero de Terreno'),
        ('mc', 'Medicion Certificada'),
    ]
    tipo = models.CharField(max_length=50, choices=OPCIONES_ENUM)
    valor = models.IntegerField(null=False)

class Alcance(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_alcance = models.CharField(max_length=100, null=False)

class SubAlcance(models.Model):
    id = models.AutoField(primary_key=True)
    id_alcance = models.ForeignKey(Alcance, on_delete=models.CASCADE, null=False)
    nombre_subalcance = models.CharField(max_length=100, null=False)

class HHDetalle(models.Model):
    id_detalle_ingenieria = models.ForeignKey(DetalleIngenieria, on_delete=models.CASCADE, null=False)
    id_hh = models.ForeignKey(HorasHombre, on_delete=models.CASCADE, null=False)
    id_subalcance = models.ForeignKey(SubAlcance, on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField(null=False)
    subtotal = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
