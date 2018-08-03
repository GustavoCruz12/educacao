from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from sortedm2m.fields import SortedManyToManyField

from thumbnail_maker.fields import ImageWithThumbnailsField


SECRETARIA_CHOICES = (
    ('gabinete', 'Gabinete'),
    ('administracao', 'Administração'),
    ('educacao', 'Educação'),
    ('infraestrutura', 'Infraestrutura'),
    ('social', 'Assistência Social'),
    ('saude', 'Saúde'),
    ('esportes', 'Esportes, Cultura e Turismo'),
)


class FotoGaleria(models.Model):
    titulo = models.CharField(verbose_name='título', max_length=50)
    imagem = ImageWithThumbnailsField(
        upload_to='galerias/',
        thumbs=('thumbs', '150x100'),
        blank=True, null=True
    )
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True)

    class Meta:
        db_table = 'tb_foto_galeria'
        verbose_name = 'Foto galeria'
        verbose_name_plural = 'Fotos galerias'
        ordering = ('-publicacao',)

    def __str__(self):
        return self.titulo


class Galeria(models.Model):
    GALERIA_CHOICES = (
        ('galeria1', 'Galeria 1'),
        ('galeria2', 'Galeria 2')
    )
    secretaria = models.CharField(verbose_name='secretaria', max_length=60, choices=SECRETARIA_CHOICES, default='administracao')
    titulo = models.CharField(verbose_name='título', max_length=80)
    slug = models.SlugField(verbose_name='URL (slug)', blank=True, null=True, max_length=80)
    imagens = SortedManyToManyField(FotoGaleria)
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True)
    secao = models.CharField(verbose_name='galeria de imagens', max_length=11, choices=GALERIA_CHOICES, default='galeria1')

    class Meta:
        db_table = 'tb_galeria'
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'
        ordering = ('-publicacao',)

    def get_absolute_url(self):
        return reverse("galerias:galeria_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(Galeria, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
