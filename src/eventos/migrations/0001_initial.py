# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaEventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Título')),
                ('slug', models.SlugField(max_length=80, verbose_name='slug automático')),
                ('secretaria', models.CharField(choices=[('gabinete', 'Gabinete'), ('administracao', 'Administração'), ('educacao', 'Educação'), ('infraestrutura', 'Infraestrutura'), ('social', 'Assistência Social'), ('saude', 'Saúde'), ('esportes', 'Esportes, Cultura e Turismo')], max_length=60, verbose_name='secretaria')),
                ('imagem', filebrowser.fields.FileBrowseField(blank=True, max_length=80, null=True, verbose_name='imagem')),
                ('texto', models.TextField(blank=True, verbose_name='Texto')),
                ('data_evento', models.DateField(verbose_name='Data do evento')),
                ('horario', models.CharField(max_length=250, verbose_name='Horário')),
            ],
            options={
                'verbose_name': 'Eventos',
                'verbose_name_plural': 'Eventos',
                'db_table': 'tb_eventos',
                'ordering': ['-data_evento'],
                'get_latest_by': 'data_evento',
            },
        ),
    ]
