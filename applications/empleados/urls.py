from django.urls import path
from . import views

app_name = "empleados_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('todos-empleados/', views.ListAllEmpleados.as_view(), name='todos'),
    path('area-empleados/<departamento>/', views.List_Empleado_by_area.as_view(), name='empleado area'),
    path('buscar-empleado/', views.List_Empleado_by_KeyWord.as_view()),
    path('habilidades/', views.List_Habilidades.as_view()),
    path('ver_empleado/<pk>/', views.Empleado_DetailView.as_view(), name='detalle'),
    path('add_empleado/', views.EmpleadoCreateView.as_view(), name='add'),
    path('exito/', views.Succes_View.as_view(), name='exito'),
    path('actualizar-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='actualizar'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete'),
    path('empleados-admin/', views.ListaEmpleados_Admin.as_view(), name='empleado admin')
]
