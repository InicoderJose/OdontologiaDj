# Generated by Django 4.1.4 on 2023-01-27 23:54

import applications.complementos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0002_alter_categoria_options_alter_especialidad_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instalaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('imgins', models.ImageField(blank=True, null=True, upload_to=applications.complementos.models.wrapper, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Instalación',
                'verbose_name_plural': 'Instalaciones',
                'ordering': ['name'],
            },
        ),
    ]