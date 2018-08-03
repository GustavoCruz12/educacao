"""urlconf for the layout application"""

from django.conf.urls import url
from .views import HomeView, NoticiaDetailView, BannerDetailView, VideoDetailView


urlpatterns =[
    url(r'^$', HomeView.as_view(), name='home_view'),

    url(r'^noticia/(?P<slug>[\-\d\w]+)/$', NoticiaDetailView.as_view(), name='noticia_detalhe'),
    url(r'^banner/(?P<slug>[\-\d\w]+)/$', BannerDetailView.as_view(), name='banner_detalhe'),
    url(r'^videos/(?P<slug>[\-\d\w]+)/$', VideoDetailView.as_view(), name='video_detalhe'),

]
