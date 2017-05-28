from django.db import models

# Create your models here.

class Alertas(models.Model):
    mensaje = models.TextField()
    usuario = models.CharField(max_length=80)
    fecha_hora_mensaje = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
       return 'Alerta: ' + self.mensaje

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"
        ordering = ('fecha_hora_mensaje',)

class AlertaRecibida(models.Model):
    alerta = models.ForeignKey(Alertas)
    leida = models.BooleanField()
    fecha_hora_mensaje_leido = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alertas recibidas"
        verbose_name_plural = "Alertas recibidas"
        ordering = ('fecha_hora_mensaje_leido',)
