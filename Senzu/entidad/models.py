from django.db import models

# Create your models here.
class Entidad(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_legal = models.CharField(max_length=160)

    class Meta:
        abstract = True
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

    def getEntidad(self):
        return self.nombre

    def __unicode__(self):
        return 'Entidad: ' + self.nombre

    def __str__(self):
        return self.getEntidad()


class Sucursal(Entidad):
    ruc = models.CharField(max_length=60)
    direccion = models.TextField(max_length=900)
    telefono = models.CharField(max_length=160)
    horario = models.TextField()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ('nombre',)

    def getSucursal(self):
        return self.ruc

    def __unicode__(self):
        return 'Sucursal: ' + self.nombre

    def __str__(self):
        return self.getSucursal()

class Sala(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300,null=True,blank=True,)
    en_lugar = models.ForeignKey(Sucursal)

    def __unicode__(self):
       return 'Sala: ' + self.nombre

    def getSala(self):
        return self.nombre + " - " + str(self.en_lugar)

    def __str__(self):
        return self.getSala()

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ('nombre',)

class Pasillo(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300,null=True,blank=True,)
    en_la_sala = models.ForeignKey(Sala)

    def __unicode__(self):
       return 'Pasillo: ' + self.nombre

    def getPasillo(self):
        return self.nombre

    def __str__(self):
        return self.getPasillo()

    class Meta:
        verbose_name = "Pasillo"
        verbose_name_plural = "Pasillos"
        ordering = ('nombre',)

class Habitacion(models.Model):
    nombre = models.CharField(max_length=160)
    detalle = models.TextField(max_length=300,null=True,blank=True,)
    en_pasillo = models.ManyToManyField(Pasillo)

    def __unicode__(self):
       return 'Habitacion: ' + self.nombre

    def getHabitacion(self):
        return self.nombre

    def __str__(self):
        return self.getHabitacion()

    class Meta:
        verbose_name= "Habitacion"
        verbose_name_plural = "Habitaciones"
        ordering = ('nombre',)