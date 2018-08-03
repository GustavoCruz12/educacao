from home.models import BannerHome, Noticia

class ComunsNoticiasMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ComunsNoticiasMixin, self).get_context_data(**kwargs)
        context["banner_principal"] = BannerHome.publicado.filter(secao='banner_principal')[:1]
        context["banner_337x280"] = BannerHome.publicado.filter(secao='banner_337x280')[:1]
        context["banner_300x400"] = BannerHome.publicado.filter(secao='banner_300x400')[:1]
        context["ultimas_noticias"] = Noticia.publicado.filter(secao='ultimas_noticias')[:1]
        context["noticias_footer_1"] = Noticia.publicado.select_related()[:3]
        context["noticias_footer_2"] = Noticia.publicado.select_related()[4:]

        return context
