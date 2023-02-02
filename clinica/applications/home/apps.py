from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.home'
    verbose_name = "Pestañas"

    def ready(self):
        from . import signals #accounts is a name of app