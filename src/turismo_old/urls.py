from django.conf.urls import url

from .views import turismo


urlpatterns = [
    # home
    url(r'^$', turismo, name='turismo'),

]
