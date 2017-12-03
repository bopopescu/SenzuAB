# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_image_de_perfil'),
        ('consultasmedicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud_de_cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('cita_para', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('A', 'Activa'), ('R', 'Rechazada'), ('C', 'Completada')], default='A', max_length=1)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Especialidad')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente')),
            ],
            options={
                'verbose_name': 'Solicitud de cita',
                'verbose_name_plural': 'Solicitudes de Citas',
                'ordering': ('cita_para',),
            },
        ),
    ]