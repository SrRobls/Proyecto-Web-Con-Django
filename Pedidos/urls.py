
from django.urls import path
from Pedidos import views
# y colocamos los urls de esta aplicacion aca
urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido")
]