'''
Created on 05/17/2017

@author: alexisbatistabustavino
'''

from rest_framework import serializers
from alertas.models import * 

class AlertasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alertas
        fields = '__all__'

class AlertasRecibidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlertaRecibida
        fields = '__all__'
