from django import forms
from .models import Empleado


# # formulario de creacion de empleado
# class pruebaForm(forms.ModelForm):
#     """Form definition for prueba."""

#     class Meta:
#         """Meta definition for pruebaform."""

#         model = Empleado
#         fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs= {
#                     'placeholder': 'Ingresa tu nombre',
#                 }
#             )
#         }
        
#     # validar informacion desde el uso de la clase form
#     def clean_first_name(self):
#         nombre = self.cleaned_data['first_name']
#         if len(nombre) < 4:
#             raise forms.ValidationError('El nombre tiene que ser mayor de 10')
        
#         return nombre