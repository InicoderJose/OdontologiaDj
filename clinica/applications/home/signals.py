from django.db.models.signals import post_save,post_delete
	#I have used django user model to use post save, post delete.
from .models import PInicio, Pclinica, Ptecnologias, Pservicio, PantesDespues, PhorarioUbicacion
from applications.empresa.models import Tecnologia, Servicio, Horario, Empleado
from applications.clientes.models import Sonrisa
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.contrib import messages

@receiver(m2m_changed,sender=PInicio.comentarios.through)
def guardar_comentarioini(sender, instance, action, **kwargs):
    data = []

    if action == "post_add":
        for a in instance.comentarios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Sonrisa.objects.all():
            if(b.pk in data):
                b.inicio = True
                b.save()
            else:
                b.inicio = False
                b.save()

    if action == "post_remove":

        for a in instance.comentarios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Sonrisa.objects.all():
            if(b.pk in data):
                b.inicio = True
                b.save()
            else:
                b.inicio = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")


@receiver(m2m_changed,sender=PInicio.empleados.through)
def guardar_empleadosini(sender, instance, action, **kwargs):
    data = []

    if action == "post_add":
        for a in instance.empleados.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Empleado.objects.all():
            if(b.pk in data):
                b.inicio = True
                b.save()
            else:
                b.inicio = False
                b.save()

    if action == "post_remove":

        for a in instance.empleados.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Empleado.objects.all():
            if(b.pk in data):
                b.inicio = True
                b.save()
            else:
                b.inicio = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")

@receiver(m2m_changed,sender=Pclinica.empleados.through)
def guardar_empleados(sender, instance, action, **kwargs):
    data = []
    if action == "post_add":
        for a in instance.empleados.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Empleado.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()

    if action == "post_remove":

        for a in instance.empleados.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Empleado.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")

@receiver(m2m_changed,sender=Ptecnologias.tecnologias.through)
def guardar_tecno(sender, instance, action, **kwargs):
    data = []
    if action == "post_add":
        print("post_Add")
        for a in instance.tecnologias.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Tecnologia.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    if action == "post_remove":
        print("post_remove")
        for a in instance.tecnologias.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Tecnologia.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")

@receiver(m2m_changed,sender=PantesDespues.sonrisas.through)
def guardar_ad(sender, instance, action, **kwargs):
    data = []
    if action == "post_add":
        
        for a in instance.sonrisas.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Sonrisa.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    if action == "post_remove":
        print("post_remove")
        for a in instance.sonrisas.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Sonrisa.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")


@receiver(m2m_changed,sender=PhorarioUbicacion.horarios.through)
def guardar_hu(sender, instance, action, **kwargs):
    data = []
    if action == "post_add":
        
        for a in instance.horarios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Horario.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()

    if action == "post_remove":
        print("post_remove")
        for a in instance.horarios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Sonrisa.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")

@receiver(m2m_changed,sender=Pservicio.servicios.through)
def guardar_servicios(sender, instance, action, **kwargs):
    data = []
    if action == "post_add":
        print("HOLA")
        for a in instance.servicios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Servicio.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()

    if action == "post_remove":
        print("post_remove")
        for a in instance.servicios.all():
            #Tecnologia.objects.filter(pk=a.pk).update(public=True)
            data.append(a.pk)
        
        for b in Servicio.objects.all():
            if(b.pk in data):
                b.public = True
                b.save()
            else:
                b.public = False
                b.save()
    
    if action == "post_clear":
        print("post_clear")
                
               
