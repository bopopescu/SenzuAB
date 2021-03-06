# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-29 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
                ('detalle', models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Pasillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=160)),
                ('detalle', models.TextField(blank=True, max_length=300, null=True)),
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
                ('detalle', models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
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
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='sala',
            name='en_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad.Sucursal'),
        ),
        migrations.AddField(
            model_name='pasillo',
            name='en_la_sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad.Sala'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='en_pasillo',
            field=models.ManyToManyField(to='entidad.Pasillo'),
        ),
    ]
