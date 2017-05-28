
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from usuarios.my_user import *

class Entidad(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_legal = models.CharField(max_length=160)
    ruc = models.CharField(max_length=60)
    direccion = models.TextField(max_length=900)
    telefono = models.CharField(max_length=160)
    horario = models.TextField()

    def __unicode__(self):
       return 'Entidad: ' + self.nombre

    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"
        ordering = ('nombre',)

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=250, unique = True)
    def __unicode__(self):
       return 'Especialidad: ' + self.especialidad

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"


class Medico(models.Model):
    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    usuario = models.ForeignKey(Usuario,limit_choices_to={'es_medico': True},)
    especialidad = models.ManyToManyField(Especialidad)
    horario = models.TextField()
    telefono = models.TextField()
    sexo = models.CharField(max_length=1, choices=GENERO)
    fecha_registrado = models.DateTimeField(auto_now_add=True)
    en_lugar = models.ManyToManyField(Entidad)

    def __unicode__(self):
       return unicode(self.usuario)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        ordering = ('usuario',)


class Paciente(models.Model):
    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    )
    usuario = models.ForeignKey(Usuario,limit_choices_to={'es_paciente': True})
    nacimiento = models.DateField()
    direccion = models.CharField(max_length=800)
    telefono = models.CharField(max_length=25,blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=3,blank=True, null=True)
    peso = models.CharField(max_length=10)
    altura = models.CharField(max_length=10)
    reacciones_alergicas = models.TextField()
    sexo = models.CharField(max_length=1, choices=GENERO)
    ocupacion = models.TextField(blank=True, null=True)
    nota_medica = models.TextField(blank=True, null=True)
    seguro_medico = models.CharField(max_length=200, blank=True, null=True)
    en_lugar = models.ManyToManyField(Entidad)

    def __unicode__(self):
       return unicode(self.usuario)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Sala(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300)
    en_lugar = models.ForeignKey(Entidad)

    def __unicode__(self):
       return 'Sala: ' + self.nombre

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ('nombre',)

class Pasillo(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300)
    en_la_sala = models.ForeignKey(Sala)

    def __unicode__(self):
       return 'Pasillo: ' + self.nombre

    class Meta:
        verbose_name = "Pasillo"
        verbose_name_plural = "Pasillos"
        ordering = ('nombre',)

class Habitacion(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300)
    en_pasillo = models.ManyToManyField(Pasillo)

    def __unicode__(self):
       return 'Habitacion: ' + self.nombre

    class Meta:
        verbose_name= "Habitacion"
        verbose_name_plural = "Habitaciones"
        ordering = ('nombre',)


class Tipo_Cita(models.Model):
    nombre = models.CharField(max_length=160)

    def __unicode__(self):
       return 'Cita: ' + self.nombre

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
    Medico = models.ForeignKey(Medico)
    habitacion = models.ForeignKey(Habitacion)
    cita_para = models.DateTimeField(auto_now=False)
    descripcion = models.TextField()
    nota_para_la_cita = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')

    def __unicode__(self):
       return 'Cita: ' + unicode(self.id)

    class Meta:
        verbose_name= "Cita"
        verbose_name_plural = "Citas"
        ordering = ('cita_para',)


class Consulta_Medica(models.Model):
    #paciente = models.ForeignKey(Paciente)
    #medico = models.ForeignKey(Medico)
    cita = models.ForeignKey(Citas)
    fecha = models.DateTimeField(auto_now=True)
    detalles = models.TextField()
    receta = models.TextField()

    def __unicode__(self):
       return 'Consultas Medicas: ' + unicode(self.id)

    class Meta:
        verbose_name= "Consulta Medica"
        verbose_name_plural = "Consultas Medicas"
        ordering = ('fecha',)