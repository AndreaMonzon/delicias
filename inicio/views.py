
# Create your views here.
from django.http import request
from django.http import response
from django.shortcuts import render
from productos.models import Producto
# Create your views here.

# Proyect Imports
#from productos.models import Producto

def inicio(request):
   
    pr_listados = Producto.objects.all()
    datos={'productos':pr_listados}
    return render(request, 'inicio/home.html',datos)


