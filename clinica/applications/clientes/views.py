from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
)

class Error505view(TemplateView):
    template_name = 'home/error_505.html'