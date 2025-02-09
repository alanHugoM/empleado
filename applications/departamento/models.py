from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre_Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        # para no registrar una combinacion dos veces
        unique_together = ('name', 'short_name') 
        
    
    def __str__(self):
        return str(self.id) + '-' + self.name

