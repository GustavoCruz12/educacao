from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from filebrowser.fields import FileBrowseField
from embed_video.fields import EmbedVideoField


STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
)

SECRETARIA_CHOICES = (
        ('gabinete', 'Gabinete'),
        ('administracao', 'Administração'),
        ('educacao', 'Educação'),
        ('infraestrutura', 'Infraestrutura'),
        ('social', 'Assistência Social'),
        ('saude', 'Saúde'),
        ('esportes', 'Esportes, Cultura e Turismo'),
)


class Gerenciador(models.Manager):
   def get_queryset(self):
       return super(Gerenciador, self).get_queryset().filter(status='publicado')


class Noticia(models.Model):

    SECAO_CHOICES = (
            ('ultimas_noticias', 'Últimas noticias'),
            ('not_destaque_1', 'Destaque 1'),
            ('not_destaque_2', 'Destaque 2'),
            ('not_secretarias', 'Secretarias'),
            ('not_antigas1', 'Antigas seção 1'),
            ('not_antigas2', 'Antigas seção 2'),
            ('not_antigas3', 'Antigas seção 3'),
            ('veja_tambem', 'Veja também'),

    )

    secretaria = models.CharField(verbose_name='secretaria', max_length=60, choices=SECRETARIA_CHOICES, default='administracao')
    titulo = models.CharField(verbose_name='título', max_length=250)
    slug = models.SlugField(verbose_name='URL (slug)', unique=True, max_length=250)
    legenda = models.CharField(verbose_name='legenda imagem')
    secao = models.CharField(verbose_name='seção', choices=SECAO_CHOICES, max_length=20)
    resumo = models.CharField(verbose_name='resumo', max_length=140, blank=True)
    conteudo = models.TextField(verbose_name='texto', blank=True)
    publicacao = models.DateTimeField(verbose_name='publicação', default=timezone.now)
    status = models.CharField(verbose_name='status', max_length=11, choices=STATUS_CHOICES, default='rascunho')
    imagem = FileBrowseField(verbose_name='image de destaque', max_length=80, directory="noticias/", blank=True, null=True)
    legenda = models.CharField(verbose_name='legenda imagem', max_length=80, blank=True, null=True)
    author = models.CharField(verbose_name='author', max_length=60, blank=True, null=True)

    objects = models.Manager()
    publicado = Gerenciador()

    class Meta:
        db_table = "tb_noticia"
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-publicacao']
        get_latest_by = '-publicacao'

    def get_absolute_url(self):
        return reverse("home:noticia_detalhe", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(Noticia, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class VideoYoutube(models.Model):
    URL_EXTERNA = (
        ('sim', 'sim'),
        ('nao', 'não'),
    )

    SECAO_CHOICES = (
        ('vid_destaque', 'Destaque'),
        ('vid_videos_2', 'Videos secão 2'),
    )

    secretaria = models.CharField(verbose_name='secretaria', max_length=60, choices=SECRETARIA_CHOICES, default='administracao')
    titulo = models.CharField(verbose_name='Titulo', max_length=250)
    slug = models.SlugField(verbose_name='URL (slug)', unique=True, max_length=250)
    url = models.URLField(verbose_name='url do video', max_length=80, null=True, blank=True)
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True)
    imagem = FileBrowseField(verbose_name="image de destaque", max_length=80, directory="videos/", blank=True, null=True,
                             help_text="200x160. Imagem para video do youtube")
    secao = models.CharField(verbose_name='seção', choices=SECAO_CHOICES, max_length=20)
    status = models.CharField(verbose_name='status', max_length=11, choices=STATUS_CHOICES, default='rascunho')
    embed = EmbedVideoField(verbose_name='embed', blank=True, null=True)
    url_externa = models.CharField(verbose_name='url externa?', max_length=3, choices=URL_EXTERNA, default='nao')
    objects = models.Manager()
    publicado = Gerenciador()

    class Meta:
        db_table = "tb_video_youtube"
        verbose_name = "Video Youtube"
        verbose_name_plural = "Videos Youtube"
        ordering = ['-publicacao']
        get_latest_by = 'publicacao'

    def get_absolute_url(self):
        return reverse("home:video_detalhe", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(VideoYoutube, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class BannerHome(models.Model):

    SECAO_CHOICES = (
        ('banner_principal', 'Banner principal'),
        ('banner_729x90',   'Banner  729x90'),
        ('banner_729x90_1', 'Banner  729x90 2'),
        ('banner_337x280', 'Banner 337x280'),
        ('banner_300x400', 'Banner 300x400'),
        ('banner_729x90_footer', 'Banner 729x90 footer')
    )

    URL_EXTERNA = (
        ('sim', 'sim'),
        ('nao', 'não'),
    )

    secretaria = models.CharField(verbose_name='secretaria', max_length=60, choices=SECRETARIA_CHOICES, default='administracao')
    titulo = models.CharField(verbose_name='Titulo', max_length=250)
    slug = models.SlugField(verbose_name='URL (slug)', unique=True, max_length=250)
    texto = models.TextField(blank=True, null=True)
    publicacao = models.DateTimeField(verbose_name='publicação', auto_now_add=True)
    banner = FileBrowseField(verbose_name="banner", max_length=80, directory="videos/", blank=True, null=True,
                             help_text="utilize o tamanho do banner de acordo com a seção")
    status = models.CharField(verbose_name='status', max_length=11, choices=STATUS_CHOICES, default='rascunho')
    url_externa = models.CharField(verbose_name='url externa?', max_length=3,choices=URL_EXTERNA, default='nao')
    secao = models.CharField(verbose_name='seção', choices=SECAO_CHOICES, max_length=20)
    url = models.URLField(verbose_name='URL', blank=True, null=True)

    objects = models.Manager()
    publicado = Gerenciador()

    def get_absolute_url(self):
        return reverse("home:banner_detalhe", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(BannerHome, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tb_home_banner'
        verbose_name = 'Banner da home'
        verbose_name_plural = 'Banners da home'
        ordering = ['-publicacao']
        get_latest_by = 'publicacao'

    def __str__(self):
        return self.titulo
