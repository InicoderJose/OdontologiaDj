from tabnanny import filename_only
from django.db import models
from applications.empresa.models import Tecnologia, Horario, Servicio, Empleado
from applications.complementos.models import Instalaciones
from applications.clientes.models import Sonrisa 
from PIL import Image
import imagehash
import os

# Create your models here.

#INICIO
class PInicio(models.Model):

    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.logo)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Home', filename)

    title = models.CharField('Titulo', max_length=50, unique=True)
    sub_title = models.CharField('Frase', max_length=50)
    image = models.ImageField('Imágen', upload_to=wrapper, blank=False, null=False)
    logo = models.ImageField('Logo', upload_to=wrapper, blank=False, null=False)
    bdescription = models.TextField('Descripción Breve', max_length=150)
    Mision = models.TextField('Misión', max_length=200, blank=True, null=True)
    vision = models.TextField('Visión', max_length=200, blank=True, null=True)
    empleados = models.ManyToManyField(Empleado, blank=True)
    servicios = models.ManyToManyField(Servicio, blank=True)
    comentarios = models.ManyToManyField(Sonrisa, blank=True)
    
    class Meta:
        verbose_name = 'P. Inicio'
        verbose_name_plural = 'P. Inicio'
        
    def __str__(self):
        return self.title

# Clinica 

class Pclinica(models.Model):
    #Cambiando nombre de imagen

    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        hash = imagehash.average_hash(Image.open(instance.image)).__str__()
        
        if hash:
            #Creando nuevo nombre
            filename = '{}.{}'.format(hash, ext) # do instance.username 

        return os.path.join('Home', filename)
        
    title = models.CharField('Titulo', max_length=50, unique=True)
    image = models.ImageField('Imágen', upload_to=wrapper, blank=False, null=False)
    description = models.TextField('Descripción extensa', max_length=500)
    instalaciones = models.ManyToManyField(Instalaciones, blank=True)
    empleados = models.ManyToManyField(Empleado, blank=True)
    public = models.BooleanField('Visible', default=False)
    

    class Meta:
        verbose_name = 'P. Clinica'
        verbose_name_plural = 'P. Clinica'
        
    def __str__(self):
        return self.title
    
    
# ==================================== 

#Servicios

class Pservicio(models.Model):
    servicios= models.ManyToManyField(Servicio, blank=True)
    public = models.BooleanField('Visible', default=False)

    class Meta:
        verbose_name = 'P. Servicios'
        verbose_name_plural = 'P. Servicios'
        
    def __str__(self):
        return "Servicio"

#=====================================

# Tecnologias

class Ptecnologias(models.Model):
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    public = models.BooleanField('Visible', default=False)

    class Meta:
        verbose_name = 'P.Tecnologías'
        verbose_name_plural = 'P. Tecnologías'

    def __str__(self):
        return "Tecnologias"

#=====================================

# Antes y Despues

class PantesDespues(models.Model):
    sonrisas = models.ManyToManyField(Sonrisa, blank=True)
    public = models.BooleanField('Visible', default=False)
    
    class Meta:
        verbose_name = 'P. Antes y Después'
        verbose_name_plural = 'P. Antes y Después'

    def __str__(self):
        return "Antes y después"

#=====================================

#Contacto

class Pcontanto(models.Model):
    wsp = models.BooleanField('whatsApp', default=False)
    email = models.BooleanField('Correo', default=False)

    class Meta:
        verbose_name = 'P. Contanto'
        verbose_name_plural = 'P. Contacto'

    def __str__(self):
        return "¿Dónde desea recibir mensajes?"
        
# Horario Ubicacion

class PhorarioUbicacion(models.Model):
    horarios = models.ManyToManyField(Horario, blank=True)
    public = models.BooleanField('Horarios Visible', default=False)
    info = models.BooleanField('Ubicación Visible', default=False)

    class Meta:
        verbose_name = 'P. Horario y Ubicación'
        verbose_name_plural = 'P. Horarios y Ubicación'

    def __str__(self):
        return "Horarios y Ubicacion"
#=====================================

def datos():
    c = Pclinica.objects.exists()
    if c:
        c = Pclinica.objects.first()
    else:
        c = "none"
    return c
