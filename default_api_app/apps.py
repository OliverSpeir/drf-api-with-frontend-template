from django.apps import AppConfig


class DefaultAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "default_api_app"
