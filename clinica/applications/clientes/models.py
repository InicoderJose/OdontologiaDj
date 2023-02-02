from django.db import models
from model_utils.models import TimeStampedModel
from .validators import text_validation, phone_validation
from PIL import Image
import imagehash
import os
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        
        if instance.image:
            hash = imagehash.average_hash(Image.open(instance.image)).__str__()

        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 
            
        return os.path.join('Clientes', filename)

def wrapper2(instance, filename):
        ext = filename.split('.')[-1]

        if instance.beforeimage:
            hash = imagehash.average_hash(Image.open(instance.beforeimage)).__str__()

        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Clientes', filename)

def wrapper3(instance, filename):
        ext = filename.split('.')[-1]

        if instance.afterimage:
            hash = imagehash.average_hash(Image.open(instance.afterimage)).__str__()

        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 
            
        return os.path.join('Clientes', filename)
# Create your models here.


# Sonrisas

class Sonrisa(TimeStampedModel):
    client = models.CharField('Cliente', max_length=30, unique=True)
    image = models.ImageField('Foto', upload_to=wrapper, blank=True, null=True)
    beforeimage = models.ImageField('Antes', upload_to=wrapper2, blank=False, null=False)
    afterimage = models.ImageField('Después', upload_to=wrapper3, blank=False, null=False)
    comment = models.TextField('Comentario', max_length=500)
    date = models.DateField(default=datetime.date.today, blank=False)
    public  = models.BooleanField('Pestaña Antes y después', default=False)
    inicio = models.BooleanField('Pestaña Inicio', default=False)

    class Meta:
        verbose_name = 'Sonrisa'
        verbose_name_plural = 'Sonrisas'
        ordering = ['client']

    def __str__(self):
        return self.client

# ====================================

#formulario

class Formulario(models.Model):
    name = models.CharField('Nombre', validators=[text_validation], max_length=30)
    email = models.EmailField('Correo')
    phone = models.CharField('Numero', validators=[phone_validation], max_length=9, unique=True)
    message = models.TextField('Mensaje', max_length=500)
    title = models.CharField('Titulo', max_length=255, blank=True)
    response = RichTextUploadingField('Respuesta', blank=True)
    read = models.BooleanField('Respondido', default=False)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.email


# ====================================
