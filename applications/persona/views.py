from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
                        TemplateView, 
                        ListView, 
                        CreateView,
                        DetailView,
                        UpdateView,
                        DeleteView
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


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida'
    ]
    success_url = reverse_lazy('persona_app:exito')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida'
    ]
    success_url = reverse_lazy('persona_app:exito')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:exito')






    
    
    
