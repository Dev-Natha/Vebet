from django.apps import AppConfig


class BetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'betapp'

    def ready(self):
        import betapp.signals
