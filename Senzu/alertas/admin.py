from django.contrib import admin

# Register your models here.
from alertas.models import *

class AlertasAdmin(admin.ModelAdmin):
    models = Alertas
    list_display = ('mensaje','usuario','fecha_hora_mensaje',)

class AlertasRecibidasAdmin(admin.ModelAdmin):
    models = AlertaRecibida
    list_display = ('alerta', 'leida','fecha_hora_mensaje_leido',)

admin.site.register(Alertas,AlertasAdmin)
admin.site.register(AlertaRecibida,AlertasRecibidasAdmin)
