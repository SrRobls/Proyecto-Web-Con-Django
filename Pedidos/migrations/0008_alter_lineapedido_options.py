# Generated by Django 4.0.6 on 2022-12-18 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0007_rename_lineapedidos_lineapedido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineapedido',
            options={'ordering': ['id'], 'verbose_name': 'Linea Pedido', 'verbose_name_plural': 'Linea Pedidos'},
        ),
    ]