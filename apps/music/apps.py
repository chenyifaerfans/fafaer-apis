from django.apps import AppConfig


class MusicConfig(AppConfig):
    name = 'music'
    verbose_name = '音乐管理'

    def ready(self):
        import music.signals
