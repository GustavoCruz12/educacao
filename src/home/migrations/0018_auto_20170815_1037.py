# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20170815_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='resumo',
            field=models.TextField(blank=True, verbose_name='resumo'),
        ),
    ]