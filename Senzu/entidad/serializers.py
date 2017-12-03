
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from django.utils import timezone
from entidad.models import *


class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"

class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = "__all__"

class PasilloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pasillo
        fields = "__all__"

class HabitacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habitacion
        fields = "__all__"
