from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    # Para relacionara sabemos que es mediante una llave foranea. asi que seria de la siguiente manere, adema con el on_delete
    # le decimo que cuando eliminamos un elemento de la tabala foranea entonces que elimine los elementos que se relacionan con ese elemento eiminado de la tabla primaria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null = True, blank = True)
    disponiblidad = models.BooleanField(default=True)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre