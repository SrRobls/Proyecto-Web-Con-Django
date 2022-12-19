from django.urls import path
# from AppWeb import views
from AppCarro import views

app_name = "carro"

urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('agregar/<int:producto_id>', views.agregar_producto_carro, name="agregar"),
    path('eliminar/<int:producto_id>', views.eliminar_producto_carro, name="eliminar"),
    path('restar/<int:producto_id>', views.restar, name="restar"),
    path('vaciar', views.vaciar_carrito, name="vaciar"),
]