__author__ = 'andrew.shvv@gmail.com'

from django.db import models


class EthereumAddress(models.CharField):
    description = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
