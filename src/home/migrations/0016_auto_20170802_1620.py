# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20170601_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=120, null=True, verbose_name='image de destaque'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='secao',
            field=models.CharField(choices=[('ultimas_noticias', 'Últimas noticias'), ('not_destaque_1', 'Destaque 1'), ('not_destaque_2', 'Destaque 2'), ('not_secretarias', 'Secretarias'), ('not_antigas1', 'Antigas seção 1'), ('not_antigas2', 'Antigas seção 2'), ('veja_tambem', 'Veja também')], max_length=20, verbose_name='seção'),
        ),
    ]
