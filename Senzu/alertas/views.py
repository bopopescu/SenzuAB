from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from alertas.serializers import * 
from rest_framework import routers, serializers, viewsets

class AlertasViewSet(viewsets.ModelViewSet):
    queryset = Alertas.objects.all()
    serializer_class = AlertasSerializer

class AlertasRecibidasViewSet(viewsets.ModelViewSet):
    queryset = AlertaRecibida.objects.all()
    serializer_class = AlertasRecibidasSerializer
