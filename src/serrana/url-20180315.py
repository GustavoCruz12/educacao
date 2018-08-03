"""serrana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin

from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', admin.site.urls),

    # thirdy part
    url(r'^captcha/', include('captcha.urls')),


    # home urls
    url(r'', include('home.urls')),
    url(r'^home/', include("home.urls", namespace='home')),
    url(r'^leis/', include("leis.urls", namespace='leis')),
    url(r'^diario-oficial/', include("diario_oficial.urls", namespace='diario_oficial')),
    url(r'^localizacao/', include("localizacao_orgaos.urls", namespace='localizacao')),
    url(r'^licitacoes/', include("licitacoes.urls", namespace='licitacoes')),
    url(r'^concursos/', include("concursos.urls", namespace='concursos')),
    url(r'^saude/', include("secretaria_saude.urls", namespace='saude')),
    url(r'^contato/', include("contato.urls", namespace='contato')),
    url(r'^transparencia/', include("transparencia.urls", namespace='transparencia')),
    url(r'^acesso-informacao/', include("acesso_informacao.urls", namespace='acesso_informacao')),
    url(r'^administracao/', include("secretaria_administracao.urls", namespace='administracao')),
    url(r'^gabinete/', include("gabinete.urls", namespace='gabinete')),
    url(r'^noticias/', include("noticias.urls", namespace='noticias')),
    url(r'^educacao/', include("secretaria_educacao.urls", namespace='educacao')),
    url(r'^infraestrutura/', include("secretaria_infra.urls", namespace='infraestrutura')),
    url(r'^social/', include("secretaria_social.urls", namespace='social')),
    url(r'^cultura-esportes-turismo/', include("secretaria_esportes.urls", namespace='esportes')),
    url(r'^serrana/', include("historia.urls", namespace='serrana')),
    url(r'^ouvidoria/', include("ouvidoria.urls", namespace='ouvidoria')),
    url(r'^emendas/', include("emendas.urls", namespace='emenda')),
    url(r'^eventos/', include("eventos.urls", namespace='eventos')),
    url(r'^galerias/', include("galeria.urls", namespace='galerias')),
    url(r'^consulta-publica/', include("consulta_publica.urls", namespace='consulta_publica')),

              ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

