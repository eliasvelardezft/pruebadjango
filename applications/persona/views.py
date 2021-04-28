from django.shortcuts import render
from django.views.generic import (
                        TemplateView, 
                        ListView, 
                        CreateView,
                        DetailView
                        )
from .models import Empleado
# Create your views here.


class EmpleadoListView(ListView):
    template_name = 'persona/empleados.html'
    paginate_by = 4
    model = Empleado
    context_object_name = 'listaEmpleados'

class ListarHojasVida(ListView):
    template_name = 'persona/hojasvida.html'
    model = Empleado
    context_object_name = 'listaHojasVida'

class EmpleadoByDeptoListView(ListView):
    template_name = 'persona/empleadospordepto.html'
    queryset = Empleado.objects.filter(
        departamento__short_name='finanzas'
    )
    context_object_name = 'listaPorDepto'
    def get_queryset(self):
        depto = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            departamento__short_name = depto
        )
        return lista

class EmpleadoByKwordListView(ListView):
    template_name = 'persona/byKeyword.html'
    model = Empleado
    context_object_name = 'listaPorKeyword'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        lista = Empleado.objects.filter(
            first_name = keyword
        )
        return lista
    
class HabilidadesByEmpleadoListView(ListView):
    template_name = 'persona/habilidadesPorEmpleado.html'
    model = Empleado
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.request.GET.get('keyword')
        if (id_empleado):    
            empleado = Empleado.objects.get(id=id_empleado)
            return empleado.habilidades.all()
        else:
            return []


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalleEmpleado.html"
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado del mes'
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    fields = '__all__'
    success_url = './agregar-empleado'


    



    
    
    
