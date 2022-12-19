from django.contrib import admin

from .models import ListaPedidos, Pedidos

# Register your models here.

admin.site.register([Pedidos, ListaPedidos])
