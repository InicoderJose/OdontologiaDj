from django.contrib import admin
from .models import Formulario, Sonrisa
from applications.empresa.models import Configuration
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from PIL import Image
import imagehash


# Register your models here.


@admin.register(Formulario)
class DocumentAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'email',
        'phone',
        'message',
        'respuesta',
        'read',
    )

    search_fields = ('name',)
    readonly_fields=('name','email','phone','message','read',)
    change_list_template = 'admin/clientes/Formulario/change_list.html'
    change_form_template = 'admin/clientes/Formulario/change_form.html'


    def respuesta(self, obj):
        res = strip_tags(obj.response)
        res = res.replace("&nbsp;", " ")
        return mark_safe(res)

    def has_add_permission(self, request, obj=None):
        return False

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False 
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
    def message_user(self, *args):
        pass

    #def get_osm_info(self):
        # ...
        #pass

    def save_model(self, request, obj, form, change):
        
        titulo = obj.title
        to = obj.email
        body = obj.response
        
        if change:
            if titulo and to and body:
                c = Configuration.objects.exists()
                a = Configuration.objects.first()
                if c:
                    backend = EmailBackend(host=a.emailhost, port=a.emailport, username=a.email, 
                    password=a.password, use_tls=a.tls, fail_silently=True)
                    backend.open()
                
                    email = EmailMultiAlternatives(titulo, body, a.email, [to], connection=backend)
                    email.attach_alternative(body, "text/html")

                    if email.send():
                        obj.read = True
                        backend.close()
                        messages.success(request, "Se envió correctamente")
                        return super().save_model(request, obj, form, change)
                    else:
                        
                        request.session["message"] = "email"
                        return super().response_change(request, obj)
                else:
                    request.session["message"] = "noe"
                    return super().response_change(request, obj)
            else:
                request.session["message"] = "vacio"
                return super().response_change(request, obj)
        

    def response_change(self, request, obj):
        #opts = obj._meta
        #print(opts.app_label)
        title = request.POST.get('title','')
        body = request.POST.get('response','')
        if not title or not body or request.session['message'] == "email" or request.session['message'] == "noe":
        
            return HttpResponseRedirect(reverse('admin:clientes_formulario_change', args=[obj.id]))
        else:
            request.session["message"] = False

        return super().response_change(request, obj)
        
    
    def changelist_view(self, request, extra_context=None):
        request.session["message"] = False
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Sonrisa)
class SonrisaAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'comment',
        'public',
        'inicio',
    )

    search_fields = ('client',)
    readonly_fields=('public', 'inicio')
    list_filter = ('public', 'inicio',)

    show_close_button = True

            
 



       