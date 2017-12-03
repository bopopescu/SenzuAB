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

class SolicitudDeCitasAdmin(admin.ModelAdmin):
    models = Solicitud_de_cita
    list_display = ('descripcion', 'paciente','cita_para','especialidad', 'estado')

admin.site.register(Tipo_Cita, TipoCitaAdmin)
admin.site.register(Citas, CitaAdmin)
admin.site.register(Consulta_Medica, ConsultaMedicaAdmin)
admin.site.register(Solicitud_de_cita,SolicitudDeCitasAdmin)
