from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import PInicio, Pclinica, Ptecnologias, Pservicio, PantesDespues, Pcontanto, PhorarioUbicacion
from applications.empresa.models import Informacion, Servicio, Tecnologia, Configuration, Empleado
from applications.clientes.models import Sonrisa
from applications.complementos.models import Oferta, Tag, Categoria
from django.utils.html import format_html
from .forms import FormularioForm
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

# Create your views here.


# Create your views here.
 # office__department=F('department')).values_list(<..FIELDS..>)

class InicioView(TemplateView):

    template_name = 'INICIO.HTML'
    #paginate_by = 3
    #queryset = Servicio.objects.filter(portada=True).order_by('id')
    #context_object_name = 'servicios'
    
    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()
        i = Oferta.objects.exists()

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.only('public').first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()
        if i == True:
            context['oferta'] = Oferta.objects.filter()
            
        

        if not a and not b and not c and not d and not e and not g and not h:
            context['vacio'] = True

        return context

class ClinicaView(TemplateView):
    template_name = 'home/CLINICA.html'

    def get_context_data(self, **kwargs):
        
        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        else:
            context['clinica'] = "noe"
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()
        
        return context




class ServListView(ListView):
    template_name = 'home/SERVICIOS.html'
    context_object_name = "servicios"
    paginate_by = 3

    def get_queryset(self):
        b = Pservicio.objects.exists()
        res = None

        if b == True:
            b = Pservicio.objects.first()

            if b.public == True:
                #kword = self.request.GET.get("inlineFormInputName",'')
                categoria = self.request.GET.get("categoria",'')
                se = self.request.GET.get("se",'')
                
                res = Servicio.objects.buscar_entrada(categoria, se)
            else:
                res = "no"
        else:
            res = "noe"

        return res 
    
    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()
        i = Categoria.objects.exists()
        j = Servicio.objects.exists()

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()
        if i == True:
            context['categorias'] = Categoria.objects.filter()
        if j == True:
            context['servtitle'] = Servicio.objects.only('title').filter(public=True)
        
        return context

class ServiceDetailView(DetailView):
    template_name = 'empresa/detailServcicio.html'
    model = Servicio
    
    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()


        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        context["servd"] = Servicio.objects.exclude(pk=self.kwargs['pk']).filter(public=True)

        return context

#Tecnologias

class TecnosListView(ListView):
    template_name = 'home/tecnologia.html'
    context_object_name = "tecno"
    paginate_by = 3 #El numero limita los caracteres

    def get_queryset(self):

        b = Ptecnologias.objects.exists()
        res = None

        if b == True:
            b = Ptecnologias.objects.first()
            if b.public == True:
                res = b.tecnologias.filter(public=True)
            else:
                res = "no"
        else:
            res = "noe"
    
        return res 

    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        return context

class TecnosDetailView(DetailView):
    template_name = 'empresa/detailTecnologias.html'
    model = Tecnologia
    
    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()


        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        context["tecnod"] = Tecnologia.objects.exclude(pk=self.kwargs['pk']).filter(public=True)

        return context

class AntesDespues(ListView):
    template_name = 'home/AntesDespues.html'
    context_object_name = "ad"
    paginate_by = 3

    def get_queryset(self):
        b = PantesDespues.objects.exists()
        
        if b:
            b = PantesDespues.objects.first()
            if b.public == True:
                res = b.sonrisas.filter(public=True)
            else:
                res = "no"
        else:
            res = "noe"

        return res 

    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.only('public').first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        return context

#Contacto

class FormularioCreateView(CreateView):
    form_class = FormularioForm
    template_name = 'home/CONTACTO.HTML'
    success_url = '.'
       

    def get_context_data(self, **kwargs):

        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()
        
        context = super().get_context_data(**kwargs)
  
        if a == True:
            context['horario'] = PhorarioUbicacion.objects.only('public').first()
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        else:
            context['contacto'] = "noe"
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        return context

#Horarios y ubicacion

class HorariosUbicacionView(TemplateView):
    template_name = 'home/Horarios.html'

    def get_context_data(self, **kwargs):
        a = PhorarioUbicacion.objects.exists()
        b = Pcontanto.objects.exists()
        c = PantesDespues.objects.exists()
        d = Ptecnologias.objects.exists()
        e = Pservicio.objects.exists()
        f = Pclinica.objects.exists()
        g = PInicio.objects.exists()
        h = Informacion.objects.exists()
       

        context = super().get_context_data(**kwargs)

        if a == True:
            context['horario'] = PhorarioUbicacion.objects.first()
        else:
            context['horario'] = "noe"
        if b == True:
            context['contacto'] = Pcontanto.objects.first()
        if c == True:
            context['ayd'] = PantesDespues.objects.only('public').first()
        if d == True:
            context['tec'] = Ptecnologias.objects.only('public').first()
        if e == True:
            context['serv'] = Pservicio.objects.only('public').first()
        if f == True:
            context['clinica'] = Pclinica.objects.first()
        if g == True:
            context['inicio'] = PInicio.objects.first()
        if h == True:
            context['info'] = Informacion.objects.first()

        return context

class Error404view(TemplateView):
    template_name = 'error404.html'

class Error405view(TemplateView):
    template_name = 'error505.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view