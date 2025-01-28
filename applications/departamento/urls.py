from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path('nuevo-dep/', views.NuevoDepartamentoView.as_view(), name='Nuevo Departameto'),
    path('lista-dep/', views.DepartamentoListView.as_view(), name='ver departamentos')
]