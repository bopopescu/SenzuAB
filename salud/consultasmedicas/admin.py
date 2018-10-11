from django.contrib import admin
from consultasmedicas.models import *
# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    models = Citas
    list_display = ('id', 'paciente', 'medico', 'fecha_creacion', 'cita_para',)


admin.site.register(Citas, CitaAdmin)
