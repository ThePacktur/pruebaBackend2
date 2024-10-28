from django.db import models

# Create your models here.

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    origenProducto = models.CharField(max_length=50)
    descripcionProducto = models.CharField(max_length=50)
    tipoProducto = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField(max_legth=15)
