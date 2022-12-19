from django.urls import path
from .views import vista_resgistro, cerrar_login, Login

# app_name = "carro"

urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('', vista_resgistro.as_view(), name="autenticacion"),
    path('cerrar_login', cerrar_login, name="cerrar_login"),
    path('Login', Login, name="Login"),
    
]