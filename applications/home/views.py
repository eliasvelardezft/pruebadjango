from django.shortcuts import render
from django.views.generic import (
                        TemplateView, 
                        ListView, 
                        CreateView
                        )
from .models import Persona
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/index.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = [x for x in range (1,11)]

class ListarPersonas(ListView):
    template_name = 'home/personas.html'
    model = Persona
    context_object_name = 'listaPersonas'


class CreatePerson(CreateView):
    model = Persona
    template_name = 'home/agregarPersona.html'
    fields = '__all__'




