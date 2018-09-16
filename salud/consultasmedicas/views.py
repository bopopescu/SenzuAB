from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from rest_framework import routers, serializers, viewsets
from usuarios.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from consultasmedicas.serializers import *
from rest_framework.permissions import *


class Tipo_CitaViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Cita.objects.all()
    serializer_class = Tipo_CitaSerializer

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class CitasPorPaciente(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        """

        :param request:
        :param format:
        :return:
        """
        estado = False
        paciente_consultado = request.data['user']
        print(paciente_consultado)
        try:
            tokenHeader = request.META.get("HTTP_AUTHORIZATION")
            tokenHeader = tokenHeader.split(" ")
            token = Token.objects.get(key=tokenHeader[1])
            usuarioToken = token.user
        except Token.DoesNotExist:
            token = None

        if token and usuarioToken.is_active:
            try:
                usuario = Usuario.objects.get(email=paciente_consultado)

            except Usuario.DoesNotExist:
                return Response({"_apiResponse_Busqueda_por": paciente_consultado, "_valido": estado,
                                 "error": "No se encontró ningún usuario"})

            try:
                paciente = Paciente.objects.get(usuario=usuario.id)

            except Paciente.DoesNotExist:
                return Response({"_apiResponse_Busqueda_por": paciente_consultado, "_valido": estado,
                                 "error": "No se encontró ningún paciente"})

            try:
                mis_citas = Citas.objects.filter(paciente=paciente.id).order_by('cita_para')
            except Citas.DoesNotExist:
                return Response({"_apiResponse_Busqueda_por": paciente_consultado, "_valido": estado,
                                 "error": "No se encontró ningúna cita"})
                mis_citas = None

            if mis_citas:
                estado = True
                serializer = MisCitasSerializer(mis_citas, many=True)
                return Response(serializer.data)
            else:
                return Response({"_apiResponse_Busqueda_por": paciente_consultado, "_valido": estado,
                                 "error": "No hay ninguna cita para este usuario"})


