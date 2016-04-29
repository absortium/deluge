__author__ = 'andrew.shvv@gmail.com'

from django.conf import settings
from django.db import models
from django.db.models import Sum
from core.utils.logging import getPrettyLogger
from ethclient import constants

logger = getPrettyLogger(__name__)


class Account(models.Model):
    """
        Comment me!
    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="accounts")

    def amount(self):
        result = Address.objects.filter(account_id=self.pk).aggregate(amount=Sum('amount'))
        if result['amount']:
            return result['amount']
        else:
            return 0

    def update(self, **kwargs):
        # update() is converted directly to an SQL statement; it doesn't call save() on the model
        # instances, and so the pre_save and post_save signals aren't emitted.
        Account.objects.filter(pk=self.pk).update(**kwargs)


class Address(models.Model):
    """
        Comment me!
    """

    amount = models.DecimalField(max_digits=constants.ACCOUNT_MAX_DIGITS,
                                 decimal_places=constants.DECIMAL_PLACES, default=0)

    address = models.CharField(max_length=50, default="0x3234234ds23e2")

    created = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, related_name="addresses")

    def update(self, **kwargs):
        # update() is converted directly to an SQL statement; it doesn't call save() on the model
        # instances, and so the pre_save and post_save signals aren't emitted.
        Address.objects.filter(pk=self.pk).update(**kwargs)
