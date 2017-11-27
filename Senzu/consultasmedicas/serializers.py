
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from django.utils import timezone
from consultasmedicas.models import *

class Tipo_CitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_Cita
        fields = "__all__"

class CitasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = "__all__"

class Consulta_MedicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consulta_Medica
        fields = "__all__"

