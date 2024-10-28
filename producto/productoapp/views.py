from django.shortcuts import render, redirect
from productoapp.models import Producto
from productoapp.forms import FormProducto
# Create your views here.
def index(request):
    return render(request, 'productoapp/index.html')

def listadoProducto(request):
    producto = Producto.objects.all()
    data = {'producto': producto}
    return render(request,'productoapp/producto.html',data)

def agregarProducto(request):
    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'productoapp/agregarproducto.html',data)

def actualizarProducto(request, id):
    producto = Producto.objects.get(id = id)
    form = FormProducto(instance=producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'productoapp/agregarproducto.html',data)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/productos')
