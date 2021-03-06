# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL (slug)')),
                ('texto', models.TextField()),
                ('publicacao', models.DateTimeField(auto_now_add=True, verbose_name='publicação')),
                ('banner', filebrowser.fields.FileBrowseField(blank=True, help_text='utilize o tamanho do banner de acordo com a seção', max_length=80, null=True, verbose_name='banner')),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=11, verbose_name='status')),
                ('url_externa', models.CharField(choices=[('sim', 'sim'), ('nao', 'não')], default='nao', max_length=3, verbose_name='url externa?')),
                ('secao', models.CharField(choices=[('banner-principal', 'Banner principal'), ('banner_2', 'Banner 2'), ('banner_3', 'Banner 3'), ('banner_4', 'Banner 4')], max_length=20, verbose_name='seção')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Banner da home',
                'verbose_name_plural': 'Banners da home',
                'db_table': 'tb_home_banner',
                'ordering': ['-publicacao'],
                'get_latest_by': 'publicacao',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretaria', models.CharField(choices=[('gabinete', 'Gabinete'), ('administracao', 'Administração'), ('educacao', 'Educação'), ('infraestrutura', 'Infraestrutura'), ('social', 'Assistência Social'), ('saude', 'Saúde'), ('esportes', 'Esportes, Cultura e Turismo')], max_length=60, verbose_name='secretaria')),
                ('titulo', models.CharField(max_length=250, verbose_name='título')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL (slug)')),
                ('secao', models.CharField(choices=[('not_destaque_1', 'Destaque 1'), ('not_destaque_2', 'Destaque 2'), ('not_secretarias', 'Secretarias'), ('not_antigas1', 'Antigas seção 1'), ('not_antigas2', 'Antigas seção 2'), ('veja_tambem', 'Veja também')], max_length=20, verbose_name='seção')),
                ('resumo', models.CharField(blank=True, max_length=140, verbose_name='resumo')),
                ('conteudo', models.TextField(blank=True, verbose_name='texto')),
                ('publicacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publicação')),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=11, verbose_name='status')),
                ('imagem', filebrowser.fields.FileBrowseField(blank=True, max_length=80, null=True, verbose_name='image de destaque')),
                ('author', models.CharField(blank=True, max_length=60, null=True, verbose_name='author')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'db_table': 'tb_noticia',
                'ordering': ['-publicacao'],
                'get_latest_by': '-publicacao',
            },
        ),
        migrations.CreateModel(
            name='VideoYoutube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='URL (slug)')),
                ('url', models.URLField(max_length=80, verbose_name='url do video')),
                ('publicacao', models.DateTimeField(auto_now_add=True, verbose_name='publicação')),
                ('imagem', filebrowser.fields.FileBrowseField(blank=True, help_text='200x160. Imagem para video do youtube', max_length=80, null=True, verbose_name='image de destaque')),
                ('secao', models.CharField(choices=[('vid_destaque', 'Destaque'), ('vid_videos_2', 'Videos secão 2')], max_length=20, verbose_name='seção')),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=11, verbose_name='status')),
                ('embed', models.TextField(blank=True, null=True, verbose_name='código embed video youtube')),
            ],
            options={
                'verbose_name': 'Video Youtube',
                'verbose_name_plural': 'Videos Youtube',
                'db_table': 'tb_video_youtube',
                'ordering': ['-publicacao'],
                'get_latest_by': 'publicacao',
            },
        ),
    ]
