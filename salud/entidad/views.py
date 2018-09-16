from entidad.models import *
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from usuarios.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from entidad.serializers import *

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class PasilloViewSet(viewsets.ModelViewSet):
    queryset = Pasillo.objects.all()
    serializer_class = PasilloSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer