from django.contrib import admin

# Register your models here.
from alertas.models import *

class AlertasAdmin(admin.ModelAdmin):
    models = Alertas

class AlertasRecibidasAdmin(admin.ModelAdmin):
    models = AlertaRecibida

admin.site.register(Alertas,AlertasAdmin)
admin.site.register(AlertaRecibida,AlertasRecibidasAdmin)
