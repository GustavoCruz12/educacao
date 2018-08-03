"""urlconf for the layout application"""

from django.conf.urls import url
from .views import EmendaParlamentarListView, EmendaParlamentarDetailView


urlpatterns =[
    url(r'^$', EmendaParlamentarListView.as_view(), name='emenda_parlamentar'),
    url(r'^detalhe/(?P<slug>[\-\d\w]+)/$', EmendaParlamentarDetailView.as_view(), name='emenda_detalhe'),
]
