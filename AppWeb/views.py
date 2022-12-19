from django.shortcuts import render

from AppCarro.models import Carro

# Create your views here.
def inicio(request):
    # return HttpResponse("Inicio")}
    carro =  Carro(request)

    return render(request, 'AppWeb/inicio.html')

# def servicios(request):
#     # return HttpResponse("Servicios")
#     return render(request, 'AppWeb/servicios.html')

# def tienda(request):
#     # return HttpResponse("Tienda")
#     return render(request, 'AppWeb/tienda.html')

# def contacto(request):
#     # return  HttpResponse("Contacto")
#     return render(request, 'AppWeb/contacto.html')