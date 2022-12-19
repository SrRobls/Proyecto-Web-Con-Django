
from django.db import models

# Create your models here.
# Creemos el modelo de Servicio
class Servicio(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=100)
    # Para poder usar imagenes debems instalar pillow, pip install pillow
    # usamos upload_to=carpeta para indicarle en que carpeta se guardara la imagen cuando creemos los objetos servicios desde el administrador
    # Notar que en la carpeta media (lla que indicamos en settings que ahi iban las imagenes) tiene una carpeta servicios con las imagnes que cargamos desde el administrador
    imagen = models.ImageField(upload_to="servicios")
    # usamos auto_now_add=True para que se autollene de acurdo al dia en que se cree o se actualize
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.titulo
