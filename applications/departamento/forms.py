from django import forms


class NuevoDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    corto_dep = forms.CharField(max_length=50)
    