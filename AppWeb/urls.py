# En este documento, añadiremos las urls de la vista de ESTA aplicacion. luego en el archivo urls
# del proyecto en general linkeamos este achivo ahi. esto nos atuda a tener mas organizado respecto
# a cual applicaion le corresponde cada url. esto obviamente, sirve para cuando trabajemos con muchas aplicaciones

# Importamos el path
from django.urls import path
from AppWeb import views
# y colocamos los urls de esta aplicacion aca
urlpatterns = [
    # con name le damos un identificador a las vistas.
    path('', views.inicio, name="inicio")
    # path('servicios', views.servicios, name="servicios"),
    # path('tienda', views.tienda, name="tienda"),
    # path('contacto', views.contacto, name="contacto")
]


# Ahora en el archivo urls del proyecto en general debemos usar include para linkear esta urls. si no, no funciona
# Ahora algoa a aclarar es que si queremos acceder a a las vistas de esta aplicacion, si o si devbeoms usar
# http://localhost:8000/[aplicaion]/[url de la vista]