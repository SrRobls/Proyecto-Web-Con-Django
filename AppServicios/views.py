
from django.shortcuts import render
from .models import Servicio

# Create your views here.
def servicios(request):
    # return HttpResponse("Servicios")
    # Traigamos los datos del modelo de servicios
    servicios = Servicio.objects.all()
    return render(request, 'AppServicios/servicios.html', {"servicios": servicios})