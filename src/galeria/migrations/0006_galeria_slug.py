# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_galeria_secretaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='slug',
            field=models.SlugField(blank=True, default='teste', max_length=80, null=True, verbose_name='URL (slug)'),
        ),
    ]
