from django.views.generic import TemplateView


class GeolocalizacaoView(TemplateView):
    template_name = 'geolocalizacao/index.html'