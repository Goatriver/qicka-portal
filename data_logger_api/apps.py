from django.apps import AppConfig


class DataLoggerApiConfig(AppConfig):
    name = 'data_logger_api'

    def ready(self):
        import data_logger_api.signals


