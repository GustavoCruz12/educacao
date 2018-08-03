from django.conf.urls import url
from .views import TipoConcursoListView, ConcursoListView, ConcursoDetailView


urlpatterns = [
    url(r'^$', TipoConcursoListView.as_view(), name='tipo_concurso_view'),
    url(r'^lista/$', ConcursoListView.as_view(), name='concurso_view'),

    url(r'^(?P<pk>[\-\d\w]+)/$', ConcursoDetailView.as_view(), name='concurso_detalhe_view'),

]
