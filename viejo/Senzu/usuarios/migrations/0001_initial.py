# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 00:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username')),
                ('cedula', models.CharField(db_index=True, max_length=60, unique=True, verbose_name='Cedula de la persona')),
                ('first_name', models.CharField(db_index=True, max_length=80, verbose_name='Nombre')),
                ('last_name', models.CharField(db_index=True, max_length=80, verbose_name='Apellido')),
                ('es_medico', models.BooleanField(default=False)),
                ('es_paciente', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'auth_user',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('cita_para', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('nota_para_la_cita', models.TextField()),
                ('estado', models.CharField(choices=[('A', 'Activa'), ('P', 'En proceso'), ('T', 'Terminada')], default='A', max_length=1)),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ('cita_para',),
            },
        ),
        migrations.CreateModel(
            name='Consulta_Medica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('detalles', models.TextField()),
                ('receta', models.TextField()),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Citas')),
            ],
            options={
                'verbose_name': 'Consulta Medica',
                'verbose_name_plural': 'Consultas Medicas',
                'ordering': ('fecha',),
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_legal', models.CharField(max_length=160)),
                ('ruc', models.CharField(max_length=60)),
                ('direccion', models.TextField(max_length=900)),
                ('telefono', models.CharField(max_length=160)),
                ('horario', models.TextField()),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
                ('detalle', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TextField()),
                ('telefono', models.TextField()),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('fecha_registrado', models.DateTimeField(auto_now_add=True)),
                ('en_lugar', models.ManyToManyField(to='usuarios.Entidad')),
                ('especialidad', models.ManyToManyField(to='usuarios.Especialidad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
                'ordering': ('usuario',),
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=800)),
                ('telefono', models.CharField(blank=True, max_length=25, null=True)),
                ('grupo_sanguineo', models.CharField(blank=True, max_length=3, null=True)),
                ('peso', models.CharField(max_length=10)),
                ('altura', models.CharField(max_length=10)),
                ('reacciones_alergicas', models.TextField()),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('ocupacion', models.TextField(blank=True, null=True)),
                ('nota_medica', models.TextField(blank=True, null=True)),
                ('seguro_medico', models.CharField(blank=True, max_length=200, null=True)),
                ('en_lugar', models.ManyToManyField(to='usuarios.Entidad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Pasillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
                ('detalle', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Pasillo',
                'verbose_name_plural': 'Pasillos',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
                ('detalle', models.TextField(max_length=300)),
                ('en_lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Entidad')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Tipo_Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
            ],
            options={
                'verbose_name': 'Tipo de cita',
                'verbose_name_plural': 'Tipos de citas',
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='pasillo',
            name='en_la_sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Sala'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='en_pasillo',
            field=models.ManyToManyField(to='usuarios.Pasillo'),
        ),
        migrations.AddField(
            model_name='citas',
            name='Medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Medico'),
        ),
        migrations.AddField(
            model_name='citas',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Habitacion'),
        ),
        migrations.AddField(
            model_name='citas',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente'),
        ),
    ]