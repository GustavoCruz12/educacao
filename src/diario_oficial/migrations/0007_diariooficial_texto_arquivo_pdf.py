# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario_oficial', '0006_auto_20180613_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='diariooficial',
            name='texto_arquivo_pdf',
            field=models.TextField(blank=True, null=True, verbose_name='texto do arquivo convertido'),
        ),
    ]