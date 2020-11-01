from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        print('check ready')
        import user.signals