# Generated by Django 4.0.6 on 2022-12-18 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppTienda', '0001_initial'),
        ('Pedidos', '0008_alter_lineapedido_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineaPedido',
            new_name='ListaPedidos',
        ),
        migrations.AlterModelOptions(
            name='listapedidos',
            options={'ordering': ['id'], 'verbose_name': 'Lista Pedido', 'verbose_name_plural': 'Lista Pedidos'},
        ),
        migrations.AlterModelTable(
            name='listapedidos',
            table='listapedidos',
        ),
    ]