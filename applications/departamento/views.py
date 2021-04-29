from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from django.urls import reverse_lazy
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/nuevodepartamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('persona_app:exito')

    def form_valid(self, form):
        print('*******new form validation*******')

        depto = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name']
        )
        depto.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job= '1',
            departamento = depto
        )

        return super(NewDepartamentoView, self).form_valid(form)
