# Generated by Django 4.1.4 on 2023-01-31 21:00

import applications.complementos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0004_rename_imgins_instalaciones_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalaciones',
            name='image',
            field=models.ImageField(upload_to=applications.complementos.models.wrapper, verbose_name='Imagen'),
        ),
    ]
