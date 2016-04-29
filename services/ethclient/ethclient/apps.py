__author__ = 'andrew.shvv@gmail.com'

from django.apps import AppConfig


class ethclientConfig(AppConfig):
    name = 'ethclient'
    verbose_name = "ethclient"

    def ready(self):
        super(ethclientConfig, self).ready()

        # This will make sure the signals is always imported when
        # Django starts so that exclude import cycles
        import ethclient.signals