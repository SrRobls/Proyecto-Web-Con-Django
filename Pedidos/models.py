from django.db import models
from django.contrib.auth import get_user_model
from AppTienda.models import Produto
from  django.db.models import F, Sum, FloatField

# Create your models here.

# Obtenemos el usuario que esta loggeado
User =  get_user_model()

class Pedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.id
    
    @property
    def total(self):
        self.listapedidos_set.aggregate(

            total = Sum(F("precio")*F("cantidad"), output_field = FloatField) 

        )["total"]
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class ListaPedidos(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'listapedidos'
        verbose_name = 'Lista Pedido'
        verbose_name_plural = 'Lista Pedidos'
        ordering = ['id']
