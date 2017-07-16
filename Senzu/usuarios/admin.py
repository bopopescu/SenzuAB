
from django.contrib import admin
from django import forms
# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.admin import widgets
from usuarios.models import *
from usuarios.my_user import *
from usuarios.forms import *

class MedicoAdm(admin.ModelAdmin):
    models= Medico

class PacienteAdmin(admin.ModelAdmin):
    models = Paciente

class EspecialidadAdmin(admin.ModelAdmin):
    models = Especialidad
    list_display = ('especialidad',)

class EntidadAdmin(admin.ModelAdmin):
    models = Entidad
    can_delete = False
    list_display = ('nombre', 'telefono','ruc',)

class SalaAdmin(admin.ModelAdmin):
    models = Sala
    list_display = ('nombre','en_lugar',)

class PasilloAdmin(admin.ModelAdmin):
    models = Pasillo
    list_display = ('nombre','en_la_sala',)

class HabitacionAdmin(admin.ModelAdmin):
    models = Habitacion
    #list_display = ('nombre','en_pasillo',)

class TipoCitaAdmin(admin.ModelAdmin):
    models = Tipo_Cita
    list_display = ('nombre',)

class CitaAdmin(admin.ModelAdmin):
    models = Citas
    list_display = ('id', 'paciente', 'medico', 'fecha_creacion', 'cita_para',)

class ConsultaMedicaAdmin(admin.ModelAdmin):
    models = Consulta_Medica
    list_display = ('cita', 'fecha', 'detalles', 'receta',)


# Now register the new UserAdmin...
admin.site.register(Usuario, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdm)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Entidad, EntidadAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Pasillo, PasilloAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Tipo_Cita, TipoCitaAdmin)
admin.site.register(Citas, CitaAdmin)
admin.site.register(Consulta_Medica, ConsultaMedicaAdmin)
