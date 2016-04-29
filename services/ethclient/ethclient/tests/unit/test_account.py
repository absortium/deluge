__author__ = 'andrew.shvv@gmail.com'

from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED

from core.utils.logging import getLogger
from ethclient.model.models import Account
from ethclient.tests.base import EthClientUnitTest

logger = getLogger(__name__)


class AccountTest(EthClientUnitTest):
    def test_creation_mixin(self):
        account = self.create_account()
        obj = Account.objects.get(pk=account['pk'])
        self.assertEqual(obj.owner, self.user)

    def test_permissions(self, *args, **kwargs):
        account = self.create_account()
        # User trying to delete account
        response = self.client.delete('/accounts/{pk}/'.format(pk=account['pk']), format='json')
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        # Create hacker user
        User = get_user_model()
        hacker = User(username="hacker")
        hacker.save()

        # Authenticate hacker
        self.client.force_authenticate(hacker)

        # Hacker trying access info of normal user account
        response = self.client.get('/accounts/{pk}/'.format(pk=account['pk']), format='json')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_malformed(self):
        trash_account_pk = "19087698021"

        # User trying to delete not created account
        response = self.client.delete('/accounts/{pk}/'.format(pk=trash_account_pk), format='json')
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        # User trying to delete not created account
        response = self.client.get('/accounts/{pk}/'.format(pk=trash_account_pk), format='json')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
