from django.urls import path
# from AppWeb import views
from AppTienda import views



urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('tienda', views.tienda, name="tienda"),
]