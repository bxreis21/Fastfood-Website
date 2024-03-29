# Generated by Django 4.0.3 on 2023-01-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0012_alter_item_valor_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='templates/images/default.jpg', upload_to='templates/media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='valor_promocional',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
