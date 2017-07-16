#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from usuarios.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from usuarios.my_user import Usuario
from usuarios.models import *

# Create your views here.
class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


# obtener los datos del usuario al enviar el username
class GetAUsuarioPorUsernameOemail(APIView):
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
        usuario_a_buscar = request.data['user']


        try:
            email = Usuario.objects.get(email = usuario_a_buscar)
        except Usuario.DoesNotExist:
            email = None
        try:
            username = Usuario.objects.get(username= usuario_a_buscar)
        except Usuario.DoesNotExist:
            username = None

        #try:
            #user = Usuario.objects.get(username= request.data['user'])

        #except Usuario.DoesNotExist:
            #user = None
        if email is not None:
            user = email
        else:
            user = username

        estado = False
        if user is not None:
            estado = True
            serializer = UserApiSerializer(user, many=False)
            return Response({"_apiResponse_Busqueda_por": usuario_a_buscar, "_estado": estado, "data": serializer.data })
        else:
            return Response({"_apiResponse_Busqueda_por": usuario_a_buscar, "_estado": estado, "error": "No se encontró ningún resultado" })
