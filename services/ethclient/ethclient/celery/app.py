from __future__ import absolute_import

__author__ = 'andrew.shvv@gmail.com'

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ethclient.settings')

from core.utils.logging import getPrettyLogger

logger = getPrettyLogger(__name__)

app = Celery('ethclient',
             broker=settings.CELERY_BROKER,
             backend=settings.CELERY_RESULT_BACKEND)

if settings.CELERY_TEST:
    """
        Because celery run in another process we should manually mock
        what we need when we test celery in integrity tests.
    """
    from ethclient.tests.mixins.celery import CeleryMockMixin
    from ethclient.tests.mixins.coinbase import CoinbaseMockMixin
    CeleryMockMixin().mock_celery()
    CoinbaseMockMixin().mock_coinbase()

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
