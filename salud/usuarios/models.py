
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from usuarios.my_user import *
from entidad.models import *


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=250, unique = True)
    def __unicode__(self):
       return 'Especialidad: ' + self.especialidad

    def getEspecialidad(self):
        return self.especialidad

    def __str__(self):
        return self.getEspecialidad()

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ('especialidad',)


class Medico(models.Model):
    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    usuario = models.OneToOneField(Usuario,limit_choices_to={'es_medico': True})
    especialidad = models.ForeignKey(Especialidad)
    horario = models.TextField()
    telefono = models.TextField()
    sexo = models.CharField(max_length=1, choices=GENERO)
    fecha_registrado = models.DateTimeField(auto_now_add=True)
    en_lugar = models.ForeignKey(Sucursal)

    def __unicode__(self):
       return unicode(self.usuario)

    def getMedico(self):
        return self.usuario

    def __str__(self):
        return str(self.getMedico())

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        ordering = ('usuario',)


class Paciente(models.Model):
    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )

    TIPO_DE_SANGRE = (
        ('O-', 'O negativo'),
        ('O+', 'O positivo'),
        ('A-', 'A negativo'),
        ('A+', 'A positivo'),
        ('B-', 'B negativo'),
        ('B+', 'B positivo'),
        ('AB-', 'AB negativo'),
        ('AB+', 'AB positivo'),
    )

    usuario = models.ForeignKey(Usuario,limit_choices_to={'es_paciente': True})
    nacimiento = models.DateField()
    direccion = models.CharField(max_length=800)
    telefono = models.CharField(max_length=25,blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=3,choices=TIPO_DE_SANGRE)
    peso = models.CharField(max_length=10)
    altura = models.CharField(max_length=10)
    reacciones_alergicas = models.TextField()
    sexo = models.CharField(max_length=1, choices=GENERO)
    ocupacion = models.TextField(blank=True, null=True)
    nota_medica = models.TextField(blank=True, null=True)
    seguro_medico = models.CharField(max_length=200, blank=True, null=True)
    en_lugar = models.ManyToManyField(Sucursal)

    def __unicode__(self):
       return unicode(self.usuario)

    def getPaciente(self):
        return self.usuario

    def __str__(self):
        return str(self.getPaciente())

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ('usuario',)

    # def save(self, *args, **kwargs):
    #     if self.nombre:
    #         self.nombre = self.nombre.capitalize()
    #     else:
    #         raise ValueError("Se debe ingresar un nombre para la Habitacion.")
    #     super(Paciente,self).save(*args,**kwargs)

class MedicoEnTurno(models.Model):
    medico = models.ForeignKey(Medico)
    entrada = models.DateTimeField(blank=False, null=False)
    salida = models.DateTimeField(blank=False, null=False)
    en_habitacion = models.ForeignKey(Habitacion)

    def __unicode__(self):
       return unicode(self.medico)

    def getMedico(self):
        return self.medico

    def __str__(self):
        return str(self.getMedico())

    class Meta:
        verbose_name = "Medico en turno"
        verbose_name_plural = "Medicos en turno"
        ordering = ('medico',)

    def se_puede_utilizar_la_habitacion(self, habitacion_consultada):
        if (habitacion_consultada == ""):
            raise ValueError("No se envio la habitacion para verificar si esta utilizada.")

        medico_en_la_habitacion = MedicoEnTurno.objects.filter( habitacion_consultada = self.en_habitacion )
        if medico_en_la_habitacion:
            if medico_en_la_habitacion.count() == 0:
                return True
            else:
                return False

    def save(self, *args, **kwargs):
        if not self.se_puede_utilizar_la_habitacion(self, self.en_habitacion):
            raise ValueError("La habitacion ya esta en uso."+ str(self.en_habitacion))
        super(MedicoEnTurno,self).save(*args,**kwargs)