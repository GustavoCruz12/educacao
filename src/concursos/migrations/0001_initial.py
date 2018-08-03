# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivosConcurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='descrição')),
                ('arquivo', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='PDF')),
                ('publicacao', models.DateTimeField(auto_now_add=True, verbose_name='publicação')),
            ],
            options={
                'verbose_name': 'Arquivos Concrusos',
                'verbose_name_plural': 'Arquivos concursos',
                'db_table': 'tb_arquivos_concurso',
            },
        ),
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=300, verbose_name='descrição')),
                ('numero', models.IntegerField(max_length=5, verbose_name='numero')),
                ('ano', models.IntegerField(max_length=4, verbose_name='ano')),
                ('observacoes', models.TextField(blank=True)),
                ('arquivos', models.ManyToManyField(to='concursos.ArquivosConcurso')),
            ],
            options={
                'verbose_name': 'Concurso',
                'verbose_name_plural': 'Concursos',
                'db_table': 'tb_concurso',
            },
        ),
        migrations.CreateModel(
            name='TipoConcurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=80, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipo',
                'db_table': 'tb_tipo_concurso',
            },
        ),
        migrations.AddField(
            model_name='concurso',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concursos.TipoConcurso'),
        ),
    ]
