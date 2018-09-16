
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
class MedicosEnTurnoAdmin(admin.ModelAdmin):
    models = MedicoEnTurno


# Now register the new UserAdmin...
admin.site.register(Usuario, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)

admin.site.register(MedicoEnTurno, MedicosEnTurnoAdmin)
admin.site.register(Medico, MedicoAdm)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)

