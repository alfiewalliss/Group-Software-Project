from django.apps import AppConfig


class LocationgameappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'locationgameapp'

class usersConfig(AppConfig):
    def ready(self):
        import users.signals