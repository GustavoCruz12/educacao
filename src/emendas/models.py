from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from filebrowser.fields import FileBrowseField


class EmendaParlamentar(models.Model):
    deputado = models.CharField(verbose_name='deputado', max_length=80)
    foto = FileBrowseField(verbose_name='foto deputado', max_length=80, directory="noticias/", blank=True, null=True)
    slug = models.SlugField(verbose_name='URL (slug)', unique=True, max_length=250)
    valor = models.CharField(verbose_name='valor', max_length=80)
    destino = models.TextField(verbose_name='destino', max_length=255)
    publicacao = models.DateTimeField(verbose_name='publicação', default=timezone.now)
    intermediador = models.CharField(verbose_name='intermediador', max_length=80, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "tb_emenda_parlamentares"
        verbose_name = "Emendas"
        verbose_name_plural = "Emendas"
        ordering = ['-publicacao']
        get_latest_by = '-publicacao'


    def get_absolute_url(self):
        return reverse("emenda:emenda_detalhe", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.deputado)
        super(EmendaParlamentar, self).save(*args, **kwargs)

    def __str__(self):
        return self.deputado


