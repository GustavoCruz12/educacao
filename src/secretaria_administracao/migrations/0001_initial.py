# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComunicadoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo')),
                ('texto', models.TextField(verbose_name='Aviso')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Publicacão')),
            ],
            options={
                'verbose_name': 'Comunicado para empresas',
                'verbose_name_plural': 'Comunicado para Empresas',
                'db_table': 'tb_comunicado_empresa',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('0', 'Manuais'), ('1', 'Decretos'), ('2', 'Instruções Normativas'), ('3', 'Legislação'), ('4', 'Formulários')], max_length=60, verbose_name='Tipo de arquivo')),
                ('descricao', models.CharField(max_length=250, verbose_name='Descrição')),
                ('observacao', models.CharField(blank=True, max_length=30, verbose_name='Observação')),
                ('arquivo', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Arquivo .doc ou .pdf')),
            ],
            options={
                'verbose_name': 'Apoio a Empresas',
                'verbose_name_plural': 'Apoio a Empresas',
                'db_table': 'tb_apoio_empresa',
            },
        ),
    ]