from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    
    
class Preventa(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    nombre_proyecto = models.CharField(max_length=100, null=False)
    nombre_solicitante = models.CharField(max_length=100, null=False)
    fecha = models.DateField(null=False)
    correlativo = models.IntegerField(null=False)
    

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100, null=False)
    nombre_especialidad = models.CharField(max_length=100, null=False)
    correo = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

class DetalleIngenieria(models.Model):
    id = models.AutoField(primary_key=True)
    id_preventa = models.ForeignKey(Preventa, on_delete=models.CASCADE, null=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    alcance = models.CharField(max_length=500, null=True)
    entregables = models.CharField(max_length=500, null=True)
    info_requerida_mandante = models.CharField(max_length=500, null=True)
    limitaciones = models.CharField(max_length=500, null=True)
    exclusiones = models.CharField(max_length=500, null=True)
    plazo_entrega = models.CharField(max_length=200, null=True)
    costo = models.IntegerField(null=False)
    firma = models.CharField(max_length=100, null=False)
    subtotal_item = models.IntegerField(null=False)
    subtotal_item_neto = models.IntegerField(null=False)
    total_item_neto = models.IntegerField(null=False)
    total_hh = models.IntegerField(null=False)

    