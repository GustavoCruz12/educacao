from django.conf.urls import url

from .views import (
    PrefeitoTemplateView,
    VicePrefeitoTemplateView
)


urlpatterns = [

    url(r'^prefeito/$', PrefeitoTemplateView.as_view(), name='prefeito'),
    url(r'^vice/$', VicePrefeitoTemplateView.as_view(), name='vice_prefeito'),

]
