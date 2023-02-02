from django.contrib import admin
from PIL import Image
import imagehash
from .models import Informacion, Servicio, Horario, Tecnologia, Configuration, Empleado
# Register your models here.


@admin.register(Tecnologia)
class TecnoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'public',
    )

    search_fields = ('title',)
    list_filter = ('public',)
    readonly_fields=('public', )
    show_close_button = True


@admin.register(Informacion)
class DocumentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        obj= Informacion.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': False,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Servicio)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'categoria',
        'public',
    )

    search_fields = ('name',)
    list_filter = ('categoria__name','public',)
    readonly_fields=('public',)
    show_close_button = True

@admin.register(Horario)
class TecnoAdmin(admin.ModelAdmin):
    readonly_fields=('public', )
    show_close_button = True

    def time_seconds(self, obj): 
        return obj.result_value.strftime("%H:%M")


@admin.register(Configuration)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = (
        'tls',
        'emailhost',
        'email',
        'password',
        'emailport',
    )

    show_close_button = True

    def has_add_permission(self, request):
        obj= Configuration.objects.all()[:1].exists()
        if obj == True:
            return False
        else:
            return True
            
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            #'show_save': False,
            'show_save_and_continue': False,
            #'show_delete': False,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'public',
        'inicio',
    )

    search_fields = ('name',)
    list_filter = ('public', 'inicio',)
    readonly_fields=('public', 'inicio',)
    show_close_button = True