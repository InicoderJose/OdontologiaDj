from django.db import models
from model_utils.models import TimeStampedModel
from PIL import Image
import imagehash
import os

def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.image)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Empresa', filename)

# Create your models here.

#Categoria

class Categoria(models.Model):
    name = models.CharField('Categoria', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name

# ====================================

# Redes

class Redes(models.Model):
    red = models.CharField(max_length=60, unique=True)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'
        ordering = ['red']

    def __str__(self):
        return self.red

# ====================================

# Oferta

class Oferta(TimeStampedModel):
    title = models.CharField('Titulo', max_length=200)
    description = models.CharField('Descripción', max_length=100, blank=True, null=True)
    image = models.ImageField('Imagen', upload_to=wrapper, blank=True, null=True)
    public = models.BooleanField('Visible', default=False)

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        ordering = ['title']

    def __str__(self):
        return self.title

# ====================================

#tag

class Tag(TimeStampedModel):
    name = models.CharField('Nombre', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
    
    def __str__(self):
        return self.name

# ====================================

# Especialidad

class Especialidad(models.Model):
    name = models.CharField('Nombre', max_length=30, unique=True)
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['name']

    def __str__(self):
        return self.name 

# ==================================== 

# Instalaciones

class Instalaciones(models.Model):
    name = models.CharField('Nombre', max_length=30)
    image = models.ImageField('Imagen', upload_to=wrapper, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Instalación'
        verbose_name_plural = 'Instalaciones'
        ordering = ['name']

    def __str__(self):
        return self.name 

# ==================================== 

