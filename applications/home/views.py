from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
    template_name ='home/home.html'
    
    

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name ='lista_prueba'
