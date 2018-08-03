# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-30 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidade', models.CharField(choices=[('BERCARIO 1', 'Berçário 1'), ('BERCARIO 2', 'Berçário 2'), ('MATERNAL 1', 'Maternal 1'), ('MATERNAL 2', 'Maternal 2')], max_length=20)),
                ('status', models.CharField(blank=True, choices=[('ATENDIDA', 'Atendida'), ('SEM CONTATO', 'Sem Contato'), ('AGUARDANDO VAGA', 'Aguardando Vaga')], max_length=20, null=True)),
                ('observacao', models.CharField(blank=True, max_length=500, null=True)),
                ('nome_crianca', models.CharField(max_length=255)),
                ('endereco_crianca', models.CharField(blank=True, max_length=255, null=True)),
                ('data_comparecimento_benedito', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Benedito')),
                ('data_comparecimento_carlosF', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Carlos França')),
                ('data_comparecimento_izildinha', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Izildinha')),
                ('data_comparecimento_lidia', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Lídia')),
                ('data_comparecimento_aparecida', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Nossa sra° Aparecida')),
                ('data_comparecimento_orestes', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Orestes')),
                ('data_comparecimento_clara', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Sta Clara')),
                ('data_comparecimento_venusta', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Venusta')),
                #('data_comparecimento_issa', models.DateField(blank=True, null=True, verbose_name='Data de Comparecimento Georgina Issa')),
                ('Benedito', models.BooleanField(verbose_name='Vaga para Benedito?')),
                ('Carlos_Franca', models.BooleanField(verbose_name='Vaga para Carlos França?')),
                ('Izildinha', models.BooleanField(verbose_name='Vaga para Izildinha?')),
                ('Lidia_Neto', models.BooleanField(verbose_name='Vaga para Lídia Neto?')),
                ('Nossa_Aparecida', models.BooleanField(verbose_name='Vaga para Nossa sr° Aparecida?')),
                ('Orestes', models.BooleanField(verbose_name='Vaga para Orestes?')),
                ('Sta_Clara', models.BooleanField(verbose_name='Vaga para Sta Clara?')),
                ('Venusta', models.BooleanField(verbose_name='Vaga para Venusta?')),
                ('GeorginaIssa', models.BooleanField(default=False, verbose_name='Vaga para Georgina?')),
                ('posicao_benedito', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno no Benedito')),
                ('posicao_carlosf', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno no Carlos França')),
                ('posicao_izildinha', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno na Izildinha')),
                ('posicao_lidia', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno na Lídia')),
                ('posicao_aparecida', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno na Nossa sra° Aparecida')),
                ('posicao_orestes', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno na Orestes')),
                ('posicao_clara', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno na Sta Clara')),
                ('posicao_venusta', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno no Venusta')),
                #('posicao_georgina', models.IntegerField(blank=True, null=True, verbose_name='Posição do aluno no GEorgina')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=255)),
                ('endereco_responsavel', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone_responsavel', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='crianca',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crianca.Responsavel'),
        ),
    ]
