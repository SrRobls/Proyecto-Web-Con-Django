from django.urls import path
# from AppWeb import views
from AppContacto import views



urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('contacto/', views.contacto, name="contacto"),
]