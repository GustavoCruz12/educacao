# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20170802_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='resumo',
            field=models.CharField(blank=True, max_length=250, verbose_name='resumo'),
        ),
    ]
