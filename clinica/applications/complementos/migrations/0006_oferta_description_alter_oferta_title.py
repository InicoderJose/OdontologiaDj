# Generated by Django 4.1.4 on 2023-02-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complementos', '0005_alter_instalaciones_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
    ]