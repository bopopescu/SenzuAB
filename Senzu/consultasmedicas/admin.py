from django.contrib import admin
from consultasmedicas.models import *
# Register your models here.



class TipoCitaAdmin(admin.ModelAdmin):
    models = Tipo_Cita
    list_display = ('nombre',)

class CitaAdmin(admin.ModelAdmin):
    models = Citas
    list_display = ('id', 'paciente', 'medico', 'fecha_creacion', 'cita_para',)

class ConsultaMedicaAdmin(admin.ModelAdmin):
    models = Consulta_Medica
    list_display = ('cita', 'fecha', 'detalles', 'receta',)

admin.site.register(Tipo_Cita, TipoCitaAdmin)
admin.site.register(Citas, CitaAdmin)
admin.site.register(Consulta_Medica, ConsultaMedicaAdmin)
