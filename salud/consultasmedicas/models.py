from django.db import models

# Create your models here.
from entidad.models import *
from usuarios.models import *
from django.conf import settings
import datetime


# def save(self, *args, **kwargs):
#     if self.nombre:
#         pass
#     else:
#         raise ValueError("Se debe ingresar un nombre para la Habitacion.")
#     super(, self).save(*args, **kwargs)



class Tipo_Cita(models.Model):
    nombre = models.CharField(max_length=160)


    def __unicode__(self):
       return 'Cita: ' + self.nombre

    def getTipoCita(self):
        return self.nombre

    def __str__(self):
        return self.getTipoCita()

    class Meta:
        verbose_name = "Tipo de cita"
        verbose_name_plural = "Tipos de citas"
        ordering = ('nombre',)

class Citas(models.Model):
    ESTADO = (
        ('A', 'Activa'),
        ('P', 'En proceso'),
        ('T', 'Terminada'),
    )
    fecha_creacion = models.DateTimeField(auto_now=True)
    paciente = models.ForeignKey(Paciente, related_name="paciente")
    medico = models.ForeignKey(Medico)
    habitacion = models.ForeignKey(Habitacion)
    cita_para = models.DateTimeField(auto_now=False)
    descripcion = models.TextField(blank=True, null=True)
    nota_para_la_cita = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')
    es_una_solicitud = models.BooleanField(default=False)

    def __unicode__(self):
       return 'Cita: ' + unicode(self.id)

    def getCitas(self):
        return self.paciente

    def __str__(self):
        return str(self.getCitas())

    class Meta:
        verbose_name= "Cita"
        verbose_name_plural = "Citas"
        ordering = ('cita_para',)

    def asignar_hora_para_la_cita(self):
        pass

    def asignar_dia_para_la_cita(self):
        pass

    def obtener_tiempo_entre_citas(self):
        TIEMPO_ENTRE_CITAS = getattr(settings, "TIEMPO_ENTRE_CITAS", None)
        return TIEMPO_ENTRE_CITAS


    def verificar_disponibilidad_del_medico(self):
        tiempo_con_min_antes = self.cita_para + datetime.timedelta(0, -self.obtener_tiempo_entre_citas())
        tiempo_con_min_despues = self.cita_para + datetime.timedelta(0,self.obtener_tiempo_entre_citas())

        citas_del_medico = Citas.objects.filter(medico = self.medico,
                                                cita_para__date=self.cita_para)

        print(citas_del_medico)

    def validar_fecha_de_la_cita(self):
        cita = Citas.objects.filter(cita_para = self.cita_para,
                                    habitacion = self.habitacion)
        self.verificar_disponibilidad_del_medico()
        if cita:
            if cita.count() == 1:
                if cita[0] == self:
                    return True
            return False
        return True

    def save(self, *args, **kwargs):
        if not self.validar_fecha_de_la_cita():
            raise ValueError("Ya existe una cita para la misma hora "+ str(self.cita_para))
        super(Citas,self).save(*args,**kwargs)
