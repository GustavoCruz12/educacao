from django.conf.urls import url
from .views import ConsultaPublicaTemplateView


urlpatterns = [
    url(r'^$', ConsultaPublicaTemplateView.as_view(), name='consulta_publica'),
    # url(r'^arquivos/$', LicitacaoListView.as_view(), name='consulta_arquivos'),

]
