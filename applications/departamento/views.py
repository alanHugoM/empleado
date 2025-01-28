from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NuevoDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento
from django.views.generic import ListView



class DepartamentoListView(ListView):
    template_name = "departamento/lista_dep.html"
    model = Departamento
    context_object_name = 'departamentos'


# Create your views here.
class NuevoDepartamentoView(FormView):
    template_name = 'departamento/new_dep.html'
    form_class = NuevoDepartamentoForm
    success_url = "/"
    
    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['corto_dep'],
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NuevoDepartamentoView, self).form_valid(form)    