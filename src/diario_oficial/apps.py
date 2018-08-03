from django.apps import AppConfig


class DiarioOficialConfig(AppConfig):
    name = 'diario_oficial'

    def ready(self):
        import diario_oficial.signals

