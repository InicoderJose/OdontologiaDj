# Generated by Django 4.1.4 on 2023-01-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_rename_especialidad_servicio_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cop',
            field=models.CharField(default='', max_length=10, verbose_name='C.O.P'),
            preserve_default=False,
        ),
    ]
