from django.urls import path, include
from . import views


app_name = 'clientes_app'

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
]