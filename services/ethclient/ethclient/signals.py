"""
    In order to avoid cycle import problem we should separate models and signals
"""

__author__ = 'andrew.shvv@gmail.com'

import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

from core.utils.logging import getPrettyLogger
from ethclient.model.models import Account

logger = getPrettyLogger(__name__, level=logging.INFO)

