# Generated by Django 4.0.3 on 2022-12-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func_mode', '0006_pedido_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='status',
        ),
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.ManyToManyField(to='func_mode.status'),
        ),
    ]