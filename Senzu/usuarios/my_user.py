'''
Created on 02/13/2017

@author: alexisbatistabustavino
'''
from __future__ import unicode_literals

from django.db import models

# http://es.stackoverflow.com/questions/930/roles-de-usuarios-en-django

# Create your models here.
from dry_rest_permissions.generics import allow_staff_or_superuser, authenticated_users
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class AdministradorDeUsuarios(BaseUserManager):
    def create_user(self, email, cedula, first_name, last_name, username):
        """
        Creates and saves a User with the given username, password, email, created_a
        birth and password.
        """

        if not cedula:
            raise ValueError('Toda persona debe tener una cedula')

        user = self.model(
            email = self.normalize_email(email),
            cedula=cedula,
            first_name=first_name,
            last_name=last_name,
            username =username
        )
        #user.set_password(password)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, password, email, cedula, first_name, last_name,username):
        user = self.create_user(email, cedula, first_name, last_name,username)
        user.is_admin = True
        #user.is_staff = True
        user.is_superuser = True
        user.email =self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=255,
        unique=True,
    )
    cedula = models.CharField(
        verbose_name = 'Cedula de la persona',
        max_length = 60,
        unique = True,
        db_index = True
        )
    first_name = models.CharField(
        verbose_name = 'Nombre',
        max_length = 80,
        db_index = True
        )
    last_name = models.CharField(
        verbose_name = 'Apellido',
        max_length = 80,
        db_index = True
        )
    es_medico = models.BooleanField(default=False)
    es_paciente = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cedula','username']

    objects = AdministradorDeUsuarios()

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return True


    @staticmethod
    def has_publish_permission(request):
        return True

    def has_object_publish_permission(self, request):
        return request.user == self.owner




    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_nombres(self):
        return self.first_name
    def get_apellidos(self):
        return self.last_name
    def get_cedula(self):
        return self.cedula
    def __str__(self):
        return self.get_full_name() + " - " + self.get_cedula()
    def tiene_permisos(self,perm, obj=None):
        return True
    def tiene_permisos_en_el_modulo(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_perfil_colaborador(self):
        perfil_colaborador = None
        if hasattr(self, 'perfilcolaborador'):
            perfil_colaborador = self.perfilcolaborador
        return perfil_colaborador

    def get_perfil_paciente(self):
        perfil_paciente = None
        if hasattr(self, 'perfilpaciente'):
            perfil_paciente = self.perfilpaciente
        return perfil_paciente

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        abstract = False
