# Generated by Django 4.0.3 on 2023-01-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0013_alter_item_img_alter_item_valor_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='templates/static/images/default.jpg', upload_to='templates/media'),
        ),
    ]