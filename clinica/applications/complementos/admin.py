from django.contrib import admin
from .models import Categoria, Redes, Oferta, Tag, Especialidad, Instalaciones

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Redes)
admin.site.register(Tag)
admin.site.register(Especialidad)
admin.site.register(Instalaciones)

@admin.register(Oferta)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'public',
    )
    
    show_close_button = True