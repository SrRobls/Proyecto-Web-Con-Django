# Generated by Django 4.0.6 on 2022-12-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0009_rename_lineapedido_listapedidos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listapedidos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
