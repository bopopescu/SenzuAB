from django.db import models

# Create your models here.
from entidad.models import *
from usuarios.models import *



class Solicitud_de_cita(models.Model):
    ESTADO = (
        ('A', 'Activa'),
        ('R', 'Rechazada'),
        ('C', 'Completada'),
    )
    paciente = models.ForeignKey(Paciente)
    fecha_creacion= models.DateTimeField(auto_now=True)
    medico = models.ForeignKey(Medico)
    cita_para = models.DateTimeField(auto_now=False)
    descripcion = models.TextField()
    especialidad = models.ForeignKey(Especialidad)
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')

    class Meta:
        verbose_name= "Solicitud de cita"
        verbose_name_plural = "Solicitudes de Citas"
        ordering = ('cita_para',)

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
    paciente = models.ForeignKey(Paciente)
    medico = models.ForeignKey(Medico)
    habitacion = models.ForeignKey(Habitacion)
    cita_para = models.DateTimeField(auto_now=False)
    descripcion = models.TextField()
    nota_para_la_cita = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')

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


class Consulta_Medica(models.Model):

    cita = models.ForeignKey(Citas)
    fecha = models.DateTimeField(auto_now=True)
    detalles = models.TextField()
    receta = models.TextField()

    def __unicode__(self):
       return 'Consultas Medicas: ' + unicode(self.id)

    def getConsultaMedica(self):
        return self.cita

    def __str__(self):
        return str(self.getConsultaMedica())

    class Meta:
        verbose_name= "Consulta Medica"
        verbose_name_plural = "Consultas Medicas"
        ordering = ('fecha',)


