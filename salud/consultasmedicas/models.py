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
        ordering = ('id',)

    def obtener_tiempo_entre_citas(self):
        TIEMPO_ENTRE_CITAS = getattr(settings, "TIEMPO_ENTRE_CITAS", None)
        return TIEMPO_ENTRE_CITAS

    def esta_disponible_el_medico(self, fecha_solicitada, medico_para_la_cita):
        if((fecha_solicitada==None) or (fecha_solicitada=="")):
            cita_con_min_antes_a_la_solicitada = (datetime.datetime.now() - datetime.timedelta(0, self.obtener_tiempo_entre_citas()))
            cita_con_min_despues_a_la_solicitada  = (datetime.datetime.now() + datetime.timedelta(0, self.obtener_tiempo_entre_citas()))
        else:
            cita_con_min_antes_a_la_solicitada = self.cita_para + datetime.timedelta(0, -self.obtener_tiempo_entre_citas())
            cita_con_min_despues_a_la_solicitada = self.cita_para + datetime.timedelta(0,self.obtener_tiempo_entre_citas())


        disponibilidad_del_medico = Citas.objects.filter(
            medico = medico_para_la_cita,
        ).filter(cita_para__range=(cita_con_min_antes_a_la_solicitada, cita_con_min_despues_a_la_solicitada))

        if disponibilidad_del_medico:

            if disponibilidad_del_medico.count() == 0:
                if disponibilidad_del_medico[0] == self:
                    raise ValueError("La cita ya se ingreso")
                return True
            else:
                return False
        else:
            return True

    def asignar_medico_para_la_cita(self, medico_para_la_cita):
        if ((medico_para_la_cita == None) or (medico_para_la_cita == "")):
            medico_sugerido = Usuario.objects.filter(
                es_medico = True,
                is_active = True
            )
            if medico_sugerido:
                if medico_sugerido.count() == 0:
                    raise ValueError("No existen medicos disponibles")
                else:
                    # TODO: se debe buscar alguna forma inteligente de asignar medicos..
                    for m in medico_sugerido:
                        if (self.esta_disponible_el_medico(self.cita_para, m)== True):
                            return medico_sugerido
                        else:
                            raise ValueError("No hay medicos en este momento")
        else:
            if(self.esta_disponible_el_medico(self.cita_para, self.medico) == True):
                return self.medico
            else:
                raise ValueError("El medico ya tiene una cita asignada para esta hora.")



    def validar_datos_de_la_cita(self):

        self.medico = self.asignar_medico_para_la_cita(self.medico)

        # TODO: aun no se valida si la habitacion esta ocupada.
        ya_valida_habitacion = False
        if(ya_valida_habitacion==True):
            cita_con_min_antes_a_la_solicitada = self.cita_para + datetime.timedelta(0, -self.obtener_tiempo_entre_citas())
            cita_con_min_despues_a_la_solicitada = self.cita_para + datetime.timedelta(0, self.obtener_tiempo_entre_citas())

            cita = Citas.objects.filter(
                habitacion = self.habitacion
            ).filter(cita_para__range=(cita_con_min_antes_a_la_solicitada, cita_con_min_despues_a_la_solicitada))
        else:
            cita = Citas.objects.filter( habitacion = self.habitacion, cita_para = self.cita_para)


        if cita:
            if cita.count() == 1:
                if cita[0] == self:
                    return True
            return False
        return True

    def save(self, *args, **kwargs):

        self.validar_datos_de_la_cita()


        if(self.fecha_creacion==""):
            raise ValueError("Las citas deben tener una fecha de creacion")
        if((self.paciente==None) or (self.paciente=="")):
            raise ValueError("Las citas deben tener un paciente")
        if((self.medico==None) or (self.medico=="")):
            raise ValueError("Las citas deben tener un medico")
        if((self.habitacion==None) or (self.habitacion=="")):
            raise ValueError("Se debe asignar una habitacion para la cita")
        if((self.cita_para==None) or (self.cita_para=="")):
            # Se debe generar una fecha para la cita
            pass

        if not self.validar_datos_de_la_cita():
            raise ValueError("No se puede crear la cita, trate cambiando la hora de la cita"+ str(self.cita_para))
        super(Citas,self).save(*args,**kwargs)
