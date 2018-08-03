from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField


SECRETARIA_CHOICES = (
        ('gabinete', 'Gabinete'),
        ('administracao', 'Administração'),
        ('educacao', 'Educação'),
        ('infraestrutura', 'Infraestrutura'),
        ('social', 'Assistência Social'),
        ('saude', 'Saúde'),
        ('esportes', 'Esportes, Cultura e Turismo'),
)

class AgendaEventos(models.Model):
    titulo = models.CharField('Título', max_length=80)
    slug = models.SlugField('slug automático', max_length=80, unique=True)
    secretaria = models.CharField(verbose_name='secretaria', max_length=60, choices=SECRETARIA_CHOICES)
    imagem = FileBrowseField(verbose_name='imagem', max_length=80, directory="eventos/", blank=True, null=True)
    texto = models.TextField('Texto', blank=True)
    data_evento = models.DateField('Data do evento')
    horario = models.CharField('Horário', max_length=250)
   
    class Meta:
        db_table = "tb_eventos"
        verbose_name = "Eventos"
        verbose_name_plural = "Eventos"
        ordering = ['-data_evento']
        get_latest_by = 'data_evento'

    def get_absolute_url(self):
        return reverse("eventos:evento_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(AgendaEventos, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
