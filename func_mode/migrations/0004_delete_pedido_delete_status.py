# Generated by Django 4.0.3 on 2022-12-31 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('func_mode', '0003_status_remove_pedido_pago_pedido_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
