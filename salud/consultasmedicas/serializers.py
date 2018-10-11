
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from django.utils import timezone
from consultasmedicas.models import *



class CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = "__all__"

class MisCitasSerializer(serializers.ModelSerializer):
    """
    Regresa las citas por el usuario consultado
    """
    fecha_creacion = serializers.DateTimeField()
    #paciente = serializers.CharField(max_length=120)
    paciente = serializers.StringRelatedField(many=False)
    medico = serializers.StringRelatedField(many=False)
    #medico = serializers.CharField(max_length=120)
    habitacion = serializers.CharField(max_length=120)
    cita_para = serializers.DateTimeField
    descripcion = serializers.CharField(max_length=120)
    nota_para_la_cita = serializers.CharField(max_length=120)
    estado = serializers.CharField(max_length=5)
    es_una_solicitud = serializers.BooleanField


    class Meta:
        model = Citas
        fields = "__all__"
