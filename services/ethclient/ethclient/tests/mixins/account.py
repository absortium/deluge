__author__ = 'andrew.shvv@gmail.com'

import decimal

from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from core.utils.logging import getPrettyLogger

logger = getPrettyLogger(__name__)


class CreateAccountMixin():
    def create_account(self, with_checks=True, user=None, debug=False):
        if user:
            # Authenticate normal user
            self.client.force_authenticate(user)
        # Create account
        response = self.client.post('/accounts/', format='json')
        if debug:
            logger.debug(response.content)

        if with_checks:
            self.assertEqual(response.status_code, HTTP_201_CREATED)

        return response.json()

    def get_account(self, currency):
        response = self.client.get('/api/accounts/', format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)

        accounts = response.json()['results']
        for account in accounts:
            if account['currency'] == currency:
                account['amount'] = decimal.Decimal(account['amount'])
                return account

    def check_account_amount(self, account, amount, user=None):
        if user:
            # Authenticate normal user
            self.client.force_authenticate(user)

        # Create account
        response = self.client.get('/api/accounts/{account_pk}/'.format(account_pk=account['pk']), format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)

        account = response.json()
        self.assertEqual(decimal.Decimal(account['amount']), decimal.Decimal(amount))
