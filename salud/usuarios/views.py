#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import os
from django.core.files import File
from rest_framework.parsers import FormParser, MultiPartParser

from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from usuarios.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from usuarios.my_user import Usuario
from usuarios.models import *
from entidad.models import *
from rest_framework.permissions import *

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class GetMedicosEnTurnos(APIView):
    def post(self, request, format=None):
        """
        """
        fecha = request.data['fecha']
        if fecha == '':
            return Response("Se debe enviar una fecha.")
        try:

            doctoresEnTurno = MedicoEnTurno.objects.filter(entrada__gte= fecha+"T0:00:00.001Z").order_by("id")
        except MedicoEnTurno.DoesNotExist:
            doctoresEnTurno = None

        if doctoresEnTurno is not None:
            serializers_doctores = MedicoEnTurnoSerializer(doctoresEnTurno, many=True, context={'request': request})
            return Response(serializers_doctores.data)
        else:
            return Response({"_apiResponse_Busqueda_por": fecha, "_valido": False, "error": "No se encontró ningún resultado" })



class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    #Permite que solo los admin y los que tiene grupo definido puedan act, crear
    #permission_classes = (UserPermission,)

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer



class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FotoDePerfilViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = FotoPerfilSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        datafile=self.request.data.get('datafile'))



class ValidarToken(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        """

        :param request:
        :param format:
        return: Bool
        """
        if request.data['token'] == "":
            return Response("Se debe enviar el token.")
        estado = False
        try:
            token = Token.objects.get(key= request.data['token'])
            usuario = token.user
        except Token.DoesNotExist:
            token = None
        if token and usuario.is_active:
            estado = True
            return Response({"valido": estado})
        return Response({"valido": estado})

class GetMedicosPorEspecialidad(APIView):
    def post(self, request, format=None):
        """
        """
        if request.data['especialidad'] =="":
            return Response("Se debe enviar la especialidad.")
        especialidad_a_buscar = request.data['especialidad']
        try:
            especialidad = Especialidad.objects.filter(especialidad= especialidad_a_buscar)

            doctores = Medico.objects.filter(especialidad= especialidad).order_by("id")
        except Medico.DoesNotExist:
            doctores = None

        if doctores is not None:
            serializers_doctores = MedicoSerializer(doctores, many=True, context={'request': request})
            return Response(serializers_doctores.data)
        else:
            return Response({"_apiResponse_Busqueda_por": especialidad_a_buscar, "_valido": False, "error": "No se encontró ningún resultado" })


# obtener los datos del usuario al enviar el username
class GetAUsuarioPorUsernameOEmail(APIView):

    def post(self, request, format=None):
        """
        /?format=json
        ---
        response_serializer: UserApiSerializer
        parameters:
            - name: Usuario
              value: Usuario
              description: Se requiere enviar el indentificador (usuario) puede ser el correo o el username
              required: true
              paramType: body
              pytype: UsernameSerializer

        """
        if request.data['user'] == "":
            return Response("Se debe enviar un usuario.")
        usuario_a_buscar = request.data['user']
        try:
            email = Usuario.objects.get(email = usuario_a_buscar)
        except Usuario.DoesNotExist:
            email = None
        try:
            username = Usuario.objects.get(username= usuario_a_buscar)
        except Usuario.DoesNotExist:
            username = None

        if email is not None:
            user = email
        else:
            user = username

        estado = False
        if user is not None:
            #estado = True
            serializer = UserApiSerializer(user, many=False)
            return Response(serializer.data)
            #return Response({"_apiResponse_Busqueda_por": usuario_a_buscar, "_valido": estado, "data": serializer.data })
        else:
            return Response({"_apiResponse_Busqueda_por": usuario_a_buscar, "_valido": estado, "error": "No se encontró ningún resultado" })

