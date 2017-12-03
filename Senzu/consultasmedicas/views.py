from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from usuarios.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from consultasmedicas.serializers import *



class Tipo_CitaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Cita.objects.all()
    serializer_class = Tipo_CitaSerializer

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class Consulta_MedicaViewSet(viewsets.ModelViewSet):
    queryset = Consulta_Medica.objects.all()
    serializer_class = Consulta_MedicaSerializer

class Solicitud_de_CitaViewSet(viewsets.ModelViewSet):
    queryset = Solicitud_de_cita.objects.all()
    serializers_class = Solicitud_de_cita