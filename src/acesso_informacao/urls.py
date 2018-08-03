"""urlconf for the layout application"""

from django.conf.urls import url
from .views import AcessoInformacaoTemplateView


urlpatterns =[
    url(r'^$', AcessoInformacaoTemplateView.as_view(), name='acesso_informacao_url'),
]
