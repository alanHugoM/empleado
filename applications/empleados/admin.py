from django.contrib import admin
from .models import Empleado, Habilidades


# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )
    def full_name(self, object):
        return object.first_name + ' ' + object.last_name
        
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades', 'departamento')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)