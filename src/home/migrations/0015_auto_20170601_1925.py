# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170601_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoyoutube',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='URL (slug)'),
        ),
    ]
