from django.db import models
from applications.departamento.models import Departamento


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad



# Create your models here.
class Empleado(models.Model):
    tipos_job = (
        ('0', 'contador'),
        ('1', 'administrador'),
        ('2', 'economista'),
        ('3', 'otro')
    )
    first_name= models.CharField('Nombre', max_length=50)
    last_name= models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Puesto', max_length=1, choices=tipos_job)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # forma interna de django para almacenar imagenes
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleado de la empresa'
        ordering = ['first_name', 'last_name']
        # para no registrar una combinacion dos veces
        unique_together = ('first_name', 'departamento')
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
