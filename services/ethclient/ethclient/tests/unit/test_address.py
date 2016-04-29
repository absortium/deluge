__author__ = 'andrew.shvv@gmail.com'

from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED

from core.utils.logging import getLogger
from ethclient.model.models import Address
from ethclient.tests.base import EthClientUnitTest

logger = getLogger(__name__)


class AddressTest(EthClientUnitTest):
    def test_creation_mixin(self):
        account = self.create_account()
        address = self.create_address(account, debug=True)

        obj = Address.objects.get(pk=address['pk'])
        self.assertEqual(obj.account_id, account['pk'])

    def test_permissions(self, *args, **kwargs):
        account = self.create_account()
        address = self.create_address(account)

        # User trying to delete address
        url = '/accounts/{account_pk}/address/{pk}'.format(account_pk=account['pk'], pk=address['pk'])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

        # Create hacker user
        User = get_user_model()
        hacker = User(username="hacker")
        hacker.save()

        # Authenticate hacker
        self.client.force_authenticate(hacker)

        # Hacker trying access info of normal user address
        url = '/accounts/{account_pk}/address/{pk}'.format(account_pk=account['pk'], pk=address['pk'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_malformed(self):
        trash_address_pk = "19087698021"

        account = self.create_account()

        # User trying to delete not created address
        url = '/accounts/{account_pk}/address/{pk}'.format(account_pk=account['pk'], pk=trash_address_pk)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

        # User trying to delete not created account
        url = '/accounts/{account_pk}/address/{pk}'.format(account_pk=account['pk'], pk=trash_address_pk)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
