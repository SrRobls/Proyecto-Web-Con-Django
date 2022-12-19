"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# Importamos estos dos para que desde el administrador podamos ver el archivo que cargamos
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # Usamos include para linker las urls de las aplicaciones
    path('AppWeb/', include('AppWeb.urls')),
    path('AppServicios/', include('AppServicios.urls')),
    path('AppContacto/', include('AppContacto.urls')),
    path('AppTienda/', include('AppTienda.urls')),
    path('Appcarro/', include('AppCarro.urls')),
    path('Registro/', include('autenticacion.urls')),
    path('Pedido/', include('Pedidos.urls'))
]

# COLOCAMOS ESTO TAMBIEN PARA VEER LAS IMAGENES CARGADAS, ESTO ES NECESARIO AYA QUE A LA HORA DE CARGAR IMAGES, SI NO ESTA ESPECIFICADA SU DIRECTORIO COMO ACA ENTONCES AL CARGAR NOS MANDA ERROR
# TAMBIE, QUE HAY QUE HACE ESTE PROCES EN EL ARCHIVO URL DEL PROYECTO Y NO DE LAS APPS
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

