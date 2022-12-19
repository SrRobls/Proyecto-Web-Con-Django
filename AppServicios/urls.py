
from django.urls import path
# from AppWeb import views
from AppServicios import views



urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('servicios', views.servicios, name="servicios"),
]

