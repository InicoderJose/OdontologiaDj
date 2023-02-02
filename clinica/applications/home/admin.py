from django.contrib import admin
from .models import PInicio, Pclinica, Pservicio, Ptecnologias, PantesDespues, Pcontanto, PhorarioUbicacion
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.html import format_html

admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.

@admin.register(PInicio)
class inicionAdmin(admin.ModelAdmin):
    filter_horizontal = ('empleados', 'servicios', 'comentarios')
    
    def has_add_permission(self, request, obj=None):
        obj= PInicio.objects.exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': True,
            #'show_delete': False,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Pclinica)
class DocumentAdmin(admin.ModelAdmin):
    filter_horizontal = ('empleados', 'instalaciones',)
    
    def has_add_permission(self, request, obj=None):
        obj= Pclinica.objects.exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': True,
            #'show_delete': False,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(Ptecnologias)
class TecnosAdmin(admin.ModelAdmin):
    list_display = (
        'Tecnologias',
        'public',
    )
    show_close_button = True
    
    filter_horizontal = ('tecnologias',)

    def Tecnologias(self, obj):
        data = ""
        for p in obj.tecnologias.all():
            data += "- " + p.title + "</br>"
        if data == "":
            return format_html("vacio")
        else:
            return format_html(data)

    def has_add_permission(self, request):
        obj= Ptecnologias.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': True,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Pservicio)
class ServAdmin(admin.ModelAdmin):
    list_display = (
        'Servicios',
        'public',
    )
    show_close_button = True

    filter_horizontal = ('servicios',)

    def Servicios(self, obj):
        data = ""
        
        for p in obj.servicios.all():
            data += "- " + p.title + "</br>"
        
        if data == "":
            return format_html("vacio")
        else:
            
            return format_html(data)
        
    def has_add_permission(self, request):
        obj= Pservicio.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': True,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(PantesDespues)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        'Sonrisas',
        'public',
    )
    show_close_button = True
    
    filter_horizontal = ('sonrisas',)
    
    def Sonrisas(self, obj):
        data = ""
        print(obj)
        for p in obj.sonrisas.all():
            data += "- " + p.client + "</br>"
        if data == "":
            return format_html("vacio")
        else:
            return format_html(data)
    

    def has_add_permission(self, request):
        obj= PantesDespues.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': True,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Pcontanto)
class PcontactoAdmin(admin.ModelAdmin):
    list_display = (
        'wsp',
        'email',
    )
    
    show_close_button = True

    def has_add_permission(self, request):
        obj= Pcontanto.objects.exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': True,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(PhorarioUbicacion)
class PhuAdmin(admin.ModelAdmin):
    list_display = (
        'Horarios',
        'public',
        'info',
    )
    
    show_close_button = True

    filter_horizontal = ('horarios',)

    def Horarios(self, obj):
        data = ""
        
        for p in obj.horarios.all():
            data += "- " + str(p) + "</br>"
        
        if data == "":
            return format_html("vacio")
        else:
            return format_html(data)

    def has_add_permission(self, request):
        obj= PhorarioUbicacion.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': True,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
