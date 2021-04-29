from django.shortcuts import render
from django.views.generic import (
                        TemplateView, 
                        ListView, 
                        CreateView
                        )
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy
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
    form_class = PersonaForm
    success_url = reverse_lazy('persona_app:exito')





