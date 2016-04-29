__author__ = 'andrew.shvv@gmail.com'

import decimal
from string import ascii_letters

from django.contrib.auth import get_user_model

from ethclient import constants
from ethclient.model.models import Account, Offer
from ethclient.tests.base import EthClientLiveTest
from core.utils.logging import getLogger

logger = getLogger(__name__)

from queue import Queue
from threading import Thread

import random


class ThreadQueue():
    threads = {}

    def __init__(self, num_worker_threads):
        self.num_worker_threads = num_worker_threads
        self.q = Queue()

    def _worker(self, name):
        while True:
            data = self.q.get()
            if data is None:
                break

            func = data["func"]
            args = data["args"]
            kwargs = data["kwargs"]

            # time.sleep(random.random())
            func(*args, **kwargs)
            self.q.task_done()

        logger.debug("Close session")
        from django import db
        db.connection.close()

    def add(self, func, *args, **kwargs):
        data = {
            "func": func,
            "args": args,
            "kwargs": kwargs
        }

        self.q.put(data)

    def start(self):
        for i in range(self.num_worker_threads):
            thread_name = "thread-{}".format(i)
            kwargs = {
                "name": thread_name
            }

            t = Thread(target=self._worker, kwargs=kwargs)
            t.quit = False
            t.start()
            self.threads[thread_name] = t

    def stop(self):
        for i in range(self.num_worker_threads):
            self.q.put(None)
        for t in self.threads:
            t.join()

    def block(self):
        # block until all tasks are done
        self.q.join()


progress_counter = 0


def django_thread_decorator(close_db=True):
    global tm

    def wrapper(func):
        def threaded_func(*args, **kwargs):
            global progress_counter
            try:
                func(*args, **kwargs)

                progress_counter += 1
                # logger.debug("Progress: {}".format(progress_counter))
            finally:
                if close_db:
                    from django.db import connection
                    connection.close()

        def decorator(*args, **kwargs):
            global tm
            tm.add(threaded_func, *args, **kwargs)

        return decorator

    return wrapper


class ThreadManager():
    threads = []

    def add(self, func, *args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        self.threads.append(t)

    def start(self):
        for t in self.threads:
            t.start()

    def stop(self):
        for t in self.threads:
            t.join()


tq = None
pool = None
tm = None


class AccuracyTest(EthClientLiveTest):
    before_dot = 10 ** (constants.MAX_DIGITS - constants.DECIMAL_PLACES) - 1
    after_dot = 10 ** constants.DECIMAL_PLACES - 1

    def random_amount(self):
        amount = -1
        while amount < constants.AMOUNT_MIN_VALUE:
            amount = decimal.Decimal('%d.%d' % (random.randint(0, self.before_dot), random.randint(0, self.after_dot)))
        return amount

    def max_amounts(self, n=10):
        return [decimal.Decimal('%d.%d' % (self.before_dot, self.after_dot)) for _ in range(n)]

    def random_amounts(self, n=10):
        return [self.random_amount() for _ in range(n)]

    def init_users(self, n):
        username_length = 20
        User = get_user_model()
        contexts = {}
        for _ in range(n):
            random_username = ''.join([random.choice(ascii_letters) for _ in range(username_length)])
            user = User(username=random_username)
            user.save()
            contexts[user] = {}
        return contexts

    def init_accounts(self, contexts):
        for user, context in contexts.items():
            self.client.force_authenticate(user)
            context['btc'] = self.get_account('btc')
            context['eth'] = self.get_account('eth')

            contexts[user] = context

        return contexts

    def check_accounts(self, contexts):
        for user, context in contexts.items():
            btc_account_amount = Account.objects.get(pk=context['btc']['pk']).amount
            eth_account_amount = Account.objects.get(pk=context['eth']['pk']).amount

            logger.debug(u"User pk: {} \n"
                         u"Account amount : {} BTC\n"
                         u"Real amount: {} BTC\n"
                         u"Account amount : {} ETH\n"
                         u"Real amount: {} ETH\n".format(user.pk,
                                                         btc_account_amount,
                                                         context['btc']['amount'],
                                                         eth_account_amount,
                                                         context['eth']['amount']))

            self.assertEqual(context['eth']['amount'], eth_account_amount)
            self.assertEqual(context['btc']['amount'], btc_account_amount)

    def check_offers(self):
        offers = Offer.objects.all()
        self.assertEqual(len(offers), 0)

    def init_deposits(self, contexts, n):
        """
            In order to ensure that exchange,withdraw tasks will not fail because
            of run out of the money we should firstly to deposit a lot of money on the accounts.
        """

        for user, context in contexts.items():
            random_deposits = self.max_amounts(10 * n)
            for deposit_amount in random_deposits:
                self.threaded_make_deposit(context['btc'], user=user, amount=deposit_amount, with_checks=False)
                self.threaded_make_deposit(context['eth'], user=user, amount=deposit_amount, with_checks=False)

            contexts[user] = context
        return contexts

    @django_thread_decorator()
    def threaded_make_deposit(self, account, *args, **kwargs):
        account['amount'] += decimal.Decimal(kwargs['amount'])
        super().make_deposit(account, *args, **kwargs)

    @django_thread_decorator()
    def threaded_create_exchange(self, account, *args, **kwargs):
        amount = decimal.Decimal(kwargs['amount'])
        price = decimal.Decimal(kwargs['price'])
        from_currency = kwargs['from_currency']
        to_currency = kwargs['to_currency']

        account[from_currency]['amount'] -= amount
        account[to_currency]['amount'] += amount * price

        super().create_exchange(*args, **kwargs)

    @django_thread_decorator()
    def threaded_make_withdrawal(self, account, *args, **kwargs):
        account['amount'] -= decimal.Decimal(kwargs['amount'])
        super().make_withdrawal(account, *args, **kwargs)

    def bombarding_withdrawal_deposit(self, contexts, n):
        for user, context in contexts.items():
            deposits = self.random_amounts(n)
            withdrawals = deposits
            exchanges = deposits

            amounts = list(zip(deposits, withdrawals, exchanges))
            for (d, w, e) in amounts:
                self.threaded_make_deposit(context['btc'], user=user, amount=d, with_checks=False)
                self.threaded_make_withdrawal(context['btc'], user=user, amount=w, with_checks=False)
                self.threaded_make_deposit(context['eth'], user=user, amount=d, with_checks=False)
                self.threaded_make_withdrawal(context['eth'], user=user, amount=w, with_checks=False)

                self.threaded_create_exchange(context,
                                              user=user,
                                              amount=e,
                                              from_currency="btc",
                                              to_currency="eth",
                                              price="1.0",
                                              with_checks=False)

                self.threaded_create_exchange(context,
                                              user=user,
                                              amount=e,
                                              from_currency="eth",
                                              to_currency="btc",
                                              price="1.0",
                                              with_checks=False)

            contexts[user] = context

        return contexts

    def test_withdrawal_deposit(self, *args, **kwargs):
        """
            In order to execute this test celery worker should use django test db, for that you shoukd set
            the CELERY_TEST=True environment variable in the worker(celery) service. See docker-compose.yml
        """

        global tm
        tm = ThreadManager()

        users_count = 10
        n = 3

        contexts = self.init_users(users_count)
        # We should wait until all users account are created (they are creating in celery)
        self.wait_celery()

        contexts = self.init_accounts(contexts)

        contexts = self.init_deposits(contexts, n)
        self.wait_celery()

        contexts = self.bombarding_withdrawal_deposit(contexts, n)
        tm.start()
        tm.stop()

        self.wait_celery()

        try:
            self.check_accounts(contexts)
            self.check_offers()
        except AssertionError:
            logger.debug("AssertionError was raised!!!")
            input("Press Enter to continue...")
