from django.views.generic import ListView, DetailView

from .models import Noticia, VideoYoutube, BannerHome
from galeria.models import Galeria
from utils.mixinscomuns import ComunsNoticiasMixin


class HomeView(ListView):
    model = Noticia
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        # contexto das home
        context = super(HomeView, self).get_context_data(**kwargs)
        context["noticia_destaque_1"] = Noticia.publicado.filter(secao='not_destaque_1')[:2]
        context["not_destaque_2"] = Noticia.publicado.filter(secao='not_destaque_2')[:1]
        context["not_secretarias_1"] = Noticia.publicado.filter(secao='not_secretarias')[:1]
        context["ultimas_noticias"] = Noticia.publicado.filter(secao='ultimas_noticias')[:3]
        context["noticias_footer_1"] = Noticia.publicado.select_related()[:3]
        context["noticias_footer_2"] = Noticia.publicado.select_related()[5:7]

        # secretarias

        # administracao
        # parte 1
        context["not_adm"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[:1]
        context["not_adm1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[1:3]

        # parte2
        context["not_adm2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[3:4]
        context["not_adm2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[5:7]

        # social
        # parte 1
        context["not_soc"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='social')[:1]
        context["not_soc1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='social')[1:3]

        # parte2
        context["not_soc2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='social')[2:3]
        context["not_soc2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='social')[3:4]

        # infraestrutura
        # parte 1
        context["not_inf"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='infraestrutura')[:1]
        context["not_inf1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='infraestrutura')[1:3]

        # parte2
        context["not_inf2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='infraestrutura')[2:3]
        context["not_inf2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='infraestrutura')[3:4]

        # saude
        # parte 1
        context["not_sa"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='saude')[:1]
        context["not_sa1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='saude')[1:3]

        # parte2
        context["not_sa2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='saude')[2:3]
        context["not_sa2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='saude')[3:4]

        # esporte
        # parte 1
        context["not_esp"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='esporte')[:1]
        context["not_esp1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='esporte')[1:3]

        # parte2
        context["not_esp2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='esporte')[2:3]
        context["not_esp2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='esporte')[3:4]

        # gabinete
        # parte 1
        context["not_gab"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='gabinete')[:1]
        context["not_gab1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='gabinete')[1:3]

        # parte2
        context["not_gab2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='gabinete')[2:3]
        context["not_gab2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='gabinete')[3:4]

        # educacao
        # parte 1
        context["not_edu"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='educacao')[:1]
        context["not_edu1"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='educacao')[1:3]

        # parte2
        context["not_edu2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='educacao')[2:3]
        context["not_edu2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='educacao')[3:4]

        # secoes de noticias antigas
        context["not_antigas"] = Noticia.publicado.filter(secao='not_antigas')[:4]

        #contexto dos videos
        context["vid_destaque"] = VideoYoutube.publicado.filter(secao='vid_destaque')[:2]
        context["vid_videos_2"] = VideoYoutube.publicado.filter(secao='vid_videos_2')[:3]

        # contexto banners
        context["banner_principal"] = BannerHome.publicado.filter(secao='banner_principal')[:1]
        context["banner_729x90"] = BannerHome.publicado.filter(secao='banner_729x90')[:1]
        context["banner_729x90_1"] = BannerHome.publicado.filter(secao='banner_729x90_1')[:1]
        context["banner_337x280"] = BannerHome.publicado.filter(secao='banner_337x280')[:1]
        context["banner_300x400"] = BannerHome.publicado.filter(secao='banner_300x400')[:1]
        context["banner_300x400"] = BannerHome.publicado.filter(secao='banner_300x400')[:1]
        context["banner_729x90_footer"] = BannerHome.publicado.filter(secao='banner_729x90_footer')[:1]


        # administracao
        # parte 1
        context["veja_tambem"] = Noticia.publicado.filter(secao='veja_tambem')[:1]
        context["veja_tambem1"] = Noticia.publicado.filter(secao='veja_tambem')[1:4]

        # parte2
        context["not_adm2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[2:3]
        context["not_adm2_2"] = Noticia.publicado.filter(secao='not_secretarias').filter(secretaria='administracao')[3:4]

        context["antigas1"] = Noticia.publicado.filter(secao='not_antigas1')[:3]

        context["antigas2"] = Noticia.publicado.filter(secao='not_antigas2')[:4]

        context["galeria1"] = Galeria.objects.select_related().filter(secao='galeria1')[:1]
        context["galeria2"] = Galeria.objects.select_related().filter(secao='galeria2')[:1]
        return context


class BannerDetailView(ComunsNoticiasMixin, DetailView):
    model = BannerHome
    template_name = "home/noticia.html"
    context_object_name = "banner"


class NoticiaDetailView(ComunsNoticiasMixin, DetailView):
    model = Noticia
    template_name = "home/noticia.html"
    context_object_name = "noticia"


class VideoDetailView(ComunsNoticiasMixin, DetailView):
    model = VideoYoutube
    template_name = "home/noticia.html"
    context_object_name = "video_youtube"