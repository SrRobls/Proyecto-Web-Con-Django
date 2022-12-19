from django.shortcuts import render
from .models import Produto

# Create your views here.
def tienda(request):
    
    productos = Produto.objects.all()
    return render(request, 'AppTienda/tienda.html', {"productos": productos})