# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-16 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='especialidad',
            options={'ordering': ('especialidad',), 'verbose_name': 'Especialidad', 'verbose_name_plural': 'Especialidades'},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ('usuario',), 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='pasillo',
            name='detalle',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
