'''
Created on 02/12/2017

@author: alexisbatistabustavino
'''
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.utils import timezone
from usuarios.my_user import *


# Serializers define the API representation.



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'username', 'email', 'is_staff', 'cedula', 'first_name', 'last_name',
                  'es_medico', 'es_paciente', 'is_active', 'is_admin', 'is_superuser')


class UserApiSerializer(serializers.HyperlinkedModelSerializer):
    """
    Respuesta de la busqueda de usuario por nombre de usuario
    """
    username = serializers.CharField(max_length=30, help_text="Require 30 caracteres o menos. Letras, digitos and @/./+/-/_ solamente.")
    first_name = serializers.CharField(max_length=80)
    last_name =serializers.CharField(max_length=80)
    email = serializers.EmailField()
    cedula = serializers.CharField(max_length=60)
    is_staff = serializers.BooleanField(default=False)
    es_medico = serializers.BooleanField(default=False)
    es_paciente = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    date_joined = serializers.DateTimeField(default=timezone.now)

    def validate(self, data):
        pass

    class Meta:
        model = Usuario
        fields = ( 'first_name', 'last_name', 'username',
        'email', 'is_staff', 'date_joined','id', 'cedula',
        'es_medico', 'es_paciente', 'is_active', 'is_superuser',
        'is_admin',
        )
