from django.contrib import admin
from .models import (
                        Noticia,
                        BannerHome,
                        VideoYoutube

                    )


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('titulo', 'secao', 'secretaria', 'publicacao', 'status')
    date_hierarchy = 'publicacao'
    list_filter = ('publicacao', 'status', 'secao')
    list_editable = ('status',)
    search_fields = ('titulo',)
    prepopulated_fields = {"slug": ("titulo",)}
    radio_fields = {"status": admin.HORIZONTAL}
    list_per_page = 20

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


@admin.register(BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao', 'secao', 'status', 'banner')
    radio_fields = {"status": admin.HORIZONTAL, "url_externa": admin.HORIZONTAL}
    prepopulated_fields = {"slug": ("titulo",)}


    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


@admin.register(VideoYoutube)
class VideoYoutubeAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)
    list_display = ('titulo', 'publicacao', 'url', 'status', 'imagem')
    prepopulated_fields = {"slug": ("titulo",)}
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'publicacao'

