# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leis', '0002_auto_20170315_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lei',
            options={'ordering': ('-numero',), 'verbose_name': 'Lei', 'verbose_name_plural': 'Leis'},
        ),
    ]
