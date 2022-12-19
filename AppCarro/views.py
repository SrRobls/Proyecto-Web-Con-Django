from AppTienda.models import Produto
from .models import Carro
from django.shortcuts import redirect

# Create your views here.

def agregar_producto_carro(request, producto_id):

    carro = Carro(request)

    producto_base_datos = Produto.objects.get(id = producto_id)

    carro.agregar(producto_base_datos)

    return redirect("tienda")

def eliminar_producto_carro(request, producto_id):

    carro = Carro(request)

    producto_base_datos = Produto.objects.get(id = producto_id)

    carro.eliminar(producto_base_datos)

    return redirect("tienda")


def restar(request, producto_id):

    carro = Carro(request)

    producto_base_datos = Produto.objects.get(id = producto_id)

    carro.restar_producto(producto_base_datos)

    return redirect("tienda")

def vaciar_carrito(request):
    carro = Carro(request)

    carro.vaciar_carro()

    return redirect("tienda")