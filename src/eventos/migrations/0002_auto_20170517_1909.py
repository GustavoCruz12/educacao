# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaeventos',
            name='slug',
            field=models.SlugField(max_length=80, unique=True, verbose_name='slug automático'),
        ),
    ]
