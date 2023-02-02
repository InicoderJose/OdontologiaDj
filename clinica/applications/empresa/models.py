# -*- coding: utf-8 -*-
from datetime import datetime
from time import strftime
from django.db import models
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .validators import phone_validation, house_validation
from ..home.managers import servicioManager
from applications.complementos.models import Tag, Redes, Especialidad, Categoria
from django.contrib.auth.models import AbstractBaseUser
from PIL import Image
import imagehash
import os

# Create your models here.

def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.image)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Tecnologias', filename)

def wrapper2(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.image)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Servicios', filename)

def wrapper3(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.image)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Empleados', filename)

# Informacion

class Informacion(models.Model):
    address = models.CharField('Direccion', max_length=60)
    district = models.CharField('Distrito', max_length=200)
    phome = models.CharField('Numero', validators=[phone_validation], max_length=9, unique=True)
    house = models.CharField('Numero Fijo', validators=[house_validation], max_length=10, unique=True)
    gmail = models.EmailField('Correo')
    redes = models.ManyToManyField(Redes)

    class Meta:
        verbose_name = 'Información'
        verbose_name_plural = 'Información'

    def __str__(self):
        return self.address

# ============================ 

# Tecnologia

class Tecnologia(models.Model):
    title = models.CharField('Nombre', max_length=30, unique=True)
    description = RichTextUploadingField('Descripción')
    image = models.ImageField('Imágen', upload_to=wrapper, blank=False, null=False, default='')
    hash = models.CharField(max_length=20, editable=False)
    public = models.BooleanField('Visible', default=False)

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        
    def __str__(self):
        return self.title

# ==================================== 

# Horarios y ubicacion

class Horario(models.Model):

    horarios= (
        ('0', 'Lunes'),
        ('1', 'Martes'),
        ('2', 'Miercoles'),
        ('3', 'Jueves'),
        ('4', 'Viernes'),
        ('5', 'Sábado'),
        ('6', 'Domingo'),
    )
    the = models.CharField('De', max_length=11, choices=horarios)
    to = models.CharField('a', max_length=11, choices=horarios, blank=True)
    of = models.TimeField('Desde')
    until = models.TimeField('Hasta')
    public = models.BooleanField('Visible', default=False)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        day = " "
        day2 = " "
        inicio = " "
        final = " "
        for c in self.the:
            if c == '0':
                day = 'Lunes'
            if c == '1':
                day = 'Martes'
            if c == '2':
                day = 'Miercoles'
            if c == '3':
                day = 'Jueves'
            if c == '4':
                day = 'Viernes'
            if c == '5':
                day = 'Sábado'
            if c == '6':
                day = 'Domingo'    
            for d in self.to:
                if d == '0':
                    day2 = 'Lunes'
                if d == '1':
                    day2 = 'Martes'
                if d == '2':
                    day2 = 'Miercoles'
                if d == '3':
                    day2 = 'Jueves'
                if d == '4':
                    day2 = 'Viernes'
                if d == '5':
                    day2 = 'Sábado'
                if d == '6':
                    day2 = 'Domingo'

        a = self.of.strftime("%H:%M")
        b = self.until.strftime("%H:%M")

        if self.of.hour >= 12 and self.of.hour <=24:
            inicio =  a + ' pm'
        else:
            inicio = a + ' am'
        
        if self.until.hour >= 12 and self.until.hour <=24:
            final =  b + ' pm'
        else:
            final = b + ' am'
        
        if day2 == " ":
            return day + ' / ' + 'Desde ' + inicio + ' hasta ' + final
        else:
            return 'De' + ' ' + day + ' a ' + day2 + ' / ' + 'Desde ' + inicio + ' hasta ' + final

# ====================================

# Servicios

class Servicio(TimeStampedModel):
    title = models.CharField('Nombre', max_length=20, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='s_cate')
    image = models.ImageField('Imagen', upload_to=wrapper2, blank=False, null=False, default='')
    description = RichTextUploadingField('Contenido')
    etiquetas = models.ManyToManyField(Tag)
    public  = models.BooleanField('Visible', default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = servicioManager()

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.title

# ====================================

#Configuracion 

class Configuration(models.Model):
    tls = models.BooleanField('EMAIL_USE_TLS',default=True, blank=False)
    emailhost = models.CharField('EMAIL_HOST',max_length=1024, default = "smtp.gmail.com", blank=False)
    email = models.EmailField('EMAIL_USER', max_length=255, blank = False)
    password = models.CharField('EMAIL_PASS', max_length=255, blank = False)
    emailport = models.PositiveSmallIntegerField('EMAIL_PORT',default=587, blank=False)

    class Meta:
        verbose_name = 'Configuración'
        verbose_name_plural = 'Configuración'


# Empleado
 
class Empleado(TimeStampedModel):
    name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellido', max_length=30)
    image = models.ImageField('Foto Perfil', upload_to=wrapper3, blank=False, null=False)
    especialidad = models.ManyToManyField(Especialidad)
    cop = models.CharField('C.O.P', max_length=10)
    public = models.BooleanField('Pestaña Clinica', default=False)
    inicio = models.BooleanField('Pestaña Inicio', default=False)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['name']
        unique_together = ('name', 'last_name')

    def __str__(self):
        return self.name + ' ' + self.last_name

# ==================================== 
