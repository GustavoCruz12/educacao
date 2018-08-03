from django.conf.urls import url
from .views import (
    AgendaEventosListView,
    AgendaEventosDetailView
)


urlpatterns = [
    # home
    url(r'^$', AgendaEventosListView.as_view(), name='evento_list'),
    url(r'^detail/(?P<slug>[\-\d\w]+)/$', AgendaEventosDetailView.as_view(), name='evento_detail'),

]
