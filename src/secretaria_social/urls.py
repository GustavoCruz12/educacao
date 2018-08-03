from django.conf.urls import url

from .views import (
    SocialNoticiaView,
    InfraestruraHomeView,
   SocialSecretarioView,
    SocialLocalizacaoList
)


urlpatterns = [
    # home
    url(r'^$', InfraestruraHomeView.as_view(), name='social'),
    url(r'^noticias/$',   SocialNoticiaView.as_view(), name='social_noticia'),
    url(r'^secretario/$', SocialSecretarioView.as_view(), name='social_secretario'),
    url(r'^localizacao/$',SocialLocalizacaoList.as_view(), name='social_localizacao'),
]
