# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-29 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('entidad', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('cita_para', models.DateTimeField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('nota_para_la_cita', models.TextField()),
                ('estado', models.CharField(choices=[('A', 'Activa'), ('P', 'En proceso'), ('T', 'Terminada')], default='A', max_length=1)),
                ('es_una_solicitud', models.BooleanField(default=False)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad.Habitacion')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ('cita_para',),
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
    ]