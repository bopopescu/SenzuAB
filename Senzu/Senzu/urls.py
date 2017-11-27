"""Senzu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from Senzu.custom_routers import HybridRouter
from alertas.views import *
from usuarios.views import *
from accounts.urls import *
from entidad.views import *
from consultasmedicas.views import *
schema_view = get_swagger_view(title='Senzu API')

router = HybridRouter()

# usuarios
router.register(r'usuarios', UserViewSet)
router.register(r'paciente', PacienteViewSet)
router.register(r'entidad', SucursalViewSet)
router.register(r'especialidad', EspecialidadViewSet)
router.register(r'medico', MedicoViewSet)
router.register(r'sala', SalaViewSet)
router.register(r'pasillo', PasilloViewSet)
router.register(r'habitacion', HabitacionViewSet)
router.register(r'tipo_cita', Tipo_CitaViewSet)
router.register(r'citas', CitasViewSet)
router.register(r'consultasmedicas', Consulta_MedicaViewSet)
router.register(r'grupos', GroupViewSet)
router.register(r'permission', PermissionViewSet)
router.add_api_view("ObetenerUsuario", url(r'ObetenerUsuario', GetAUsuarioPorUsernameOemail.as_view(), name="ObetenerUsuario"))
router.add_api_view('ValidarToken', url(r'ValidarToken', ValidarToken.as_view(), name="ValidarToken"))

# Alertas
router.register(r'alertas', AlertasViewSet)
router.register(r'alertasRecibida', AlertasRecibidasViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api_v1/', include(router.urls)),
    #url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] +urlpatternsAccount + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
