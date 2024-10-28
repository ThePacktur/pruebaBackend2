from django.contrib import admin
from productoapp.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto','origenProducto','descripcionProducto','tipoProducto','cantidadProducto']

# Register your models here.

admin.site.register(Producto, ProductoAdmin)
