from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home_app'

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'contacto-form', 
        views.FormularioCreateView.as_view(), 
        name='contacto'
    ),
    path(
        'Horario-ubicacion', 
        views.HorariosUbicacionView.as_view(), 
        name='horarioUbicacion'
    ),
    path(
        'clínica', 
        views.ClinicaView.as_view(), 
        name='clinica'
    ),
    path(
        'Antes-Despues', 
        views.AntesDespues.as_view(), 
        name='antesdespues'
    ),
    path(
        'dtecnologias/<pk>/', 
        views.TecnosDetailView.as_view(), 
        name='tecnologias-detail'
    ),
    path(
        'tecnologias', 
        views.TecnosListView.as_view(), 
        name='tecnos-list'
    ),
    path(
        'dservicios/<pk>/', 
        views.ServiceDetailView.as_view(), 
        name='service-detail'
    ),
    path(
        'servicios', 
        views.ServListView.as_view(), 
        name='servicios-list'
    ),
]

