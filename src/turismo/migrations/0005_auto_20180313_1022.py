# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-03-13 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0004_auto_20180313_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracao',
            old_name='tipo',
            new_name='tag',
        ),
    ]
