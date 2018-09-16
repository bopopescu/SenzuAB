from django.contrib import admin
from entidad.models import *
# Register your models here.

class SucursalAdmin(admin.ModelAdmin):
    models = Sucursal

class SalaAdmin(admin.ModelAdmin):
    models = Sala
    list_display = ('nombre','en_lugar',)

class PasilloAdmin(admin.ModelAdmin):
    models = Pasillo
    list_display = ('nombre','en_la_sala',)

class HabitacionAdmin(admin.ModelAdmin):
    models = Habitacion
    #list_display = ('nombre','en_pasillo',)


admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Pasillo, PasilloAdmin)
admin.site.register(Habitacion, HabitacionAdmin)