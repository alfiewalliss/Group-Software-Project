from django.apps import AppConfig


class LocationgameappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locationgameapp'

    def ready(self):
        import locationgameapp.signals
    