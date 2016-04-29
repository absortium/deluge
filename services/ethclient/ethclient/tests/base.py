__author__ = 'andrew.shvv@gmail.com'

import time

from django.contrib.auth import get_user_model
from django.test import override_settings
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase, APIClient, APITransactionTestCase

from core.utils.logging import getLogger
from ethclient import celery_app
from ethclient.tests.mixins.account import CreateAccountMixin
from ethclient.tests.mixins.address import CreateAddressMixin
from ethclient.tests.mixins.router import RouterMockMixin

logger = getLogger(__name__)


class EthClientTestMixin():
    def get_first(self, response):
        self.assertEqual(response.status_code, HTTP_200_OK)

        json = response.json()
        results = json['results']

        self.assertGreaterEqual(len(results), 0)

        return results[0]


class EthClientLiveTest(APITransactionTestCase,
                        EthClientTestMixin,
                        CreateAccountMixin,
                        CreateAddressMixin):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

    def wait_celery(self, tag=None):
        # WARNING: Sometime may skip the execution and I don't know why
        i = celery_app.control.inspect()

        def queue_not_empty():
            queues = i.active()

            if not queues:
                raise Exception("Celery was stopped!")

            queue_empty = True
            for name, tasks in queues.items():
                if tasks:
                    queue_empty = False

            if tag:
                logger.debug("Wait for '{}'...".format(tag, queue_empty))

            return not queue_empty

        # i.active() may return empty list but process is not over
        # so lets check several times :)

        times = 3
        while all([queue_not_empty() for _ in range(times)]):
            time.sleep(0.2)


@override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                   CELERY_ALWAYS_EAGER=True)
class EthClientUnitTest(APITestCase,
                        EthClientTestMixin,
                        CreateAccountMixin,
                        RouterMockMixin,
                        CreateAddressMixin):
    def setUp(self):
        super().setUp()
        self.mock_router()

        # WARNING: User creation should be after mocking the coinbase, because there is user signal which creates the accounts.
        User = get_user_model()
        user = User(username="primary", password="test")
        user.save()

        self.user = user
        self.client = APIClient()
        self.client.force_authenticate(user)

    def tearDown(self):
        self.unmock_router()
        super().tearDown()


import threading


def test_concurrently(times):
    """
    Add this decorator to small pieces of code that you want to test
    concurrently to make sure they don't raise exceptions when run at the
    same time.  E.g., some Django views that do a SELECT and then a subsequent
    INSERT might fail when the INSERT assumes that the data has not changed
    since the SELECT.
    """

    def test_concurrently_decorator(test_func):
        def wrapper(*args, **kwargs):
            exceptions = []

            def call_test_func():
                try:
                    test_func(*args, **kwargs)
                except Exception as e:
                    exceptions.append(e)
                    raise

            threads = []
            for i in range(times):
                threads.append(threading.Thread(target=call_test_func))
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            if exceptions:
                raise Exception('test_concurrently intercepted %s exceptions: %s' % (len(exceptions), exceptions))

        return wrapper

    return test_concurrently_decorator
