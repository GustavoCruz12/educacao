# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leis', '0003_auto_20170530_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lei',
            options={'verbose_name': 'Lei', 'verbose_name_plural': 'Leis'},
        ),
        migrations.AlterField(
            model_name='lei',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
