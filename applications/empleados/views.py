from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from django.urls import reverse_lazy
from django.contrib import messages
# personalizar el form del html
# from .forms import pruebaForm 

# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    context_object_name = 'lista' # se manda al html para poder accesarlo
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista


class ListaEmpleados_Admin(ListView):
    template_name = 'empleados/empleado_admin.html'
    paginate_by = 8
    ordering = 'first_name'
    context_object_name = 'empleados' # se manda al html para poder accesarlo
    model = Empleado


class List_Empleado_by_area(ListView):
    template_name = 'empleados/list_departamento.html'
    context_object_name ='empleados'

    def get_queryset(self):
        area = self.kwargs['departamento']
        lista = Empleado.objects.filter(
            departamento__name = area
        )
        return lista


class List_Empleado_by_KeyWord(ListView):
    template_name = 'empleados/list_key.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('******')
        palabra_clave = self.request.GET.get('kword', '')
        print('====', palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista
    

class List_Habilidades(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        # pass
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()


class Empleado_DetailView(DetailView):
    model = Empleado
    template_name = "empleados/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(Empleado_DetailView, self).get_context_data(**kwargs)
        context['Titulo'] = 'Empleado del mes'
        return context



class Succes_View(TemplateView):
    template_name = "empleados/exito_add.html"


class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    fields = [
        'first_name', 
        'last_name', 
        'job', 
        'departamento', 
        'habilidades',
        'avatar'] # los llamamos desde el form.py
    # success_url = "."
    # success_url = "/exito/"
    # form_class = pruebaForm
    success_url = reverse_lazy("empleados_app:add")

    def form_valid(self, form):
        # empleado = form.save()
        empleado = form.save(commit=False) # para no guardar dos veces dentro de la misma funcion
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() # hace uso del orm de django
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/actualizar.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy("empleados_app:empleado admin")
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

class EmpleadoDeleteView(DeleteView):
    template_name = "empleados/delete.html"
    model = Empleado
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy("empleados_app:empleado admin")
