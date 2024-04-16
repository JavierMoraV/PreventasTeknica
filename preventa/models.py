from django.db import models

class Proyecto(models.Model):
    cliente = models.CharField(max_length=100)
    proyecto = models.CharField(max_length=100)
    solicitante = models.CharField(max_length=100)
    fecha = models.DateField()
    correlativo = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente  # O cualquier campo que desees mostrar en la representación del objeto

