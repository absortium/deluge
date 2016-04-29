__author__ = 'andrew.shvv@gmail.com'
import binascii
import hashlib

from django.conf import settings
from django.db import transaction
from rest_framework import mixins, viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import NotFound, PermissionDenied

from core.utils.logging import getPrettyLogger
from ethclient.model.models import Account
from ethclient.serializer.serializers import AccountSerializer, AddressSerializer

logger = getPrettyLogger(__name__)
from ethclient.rpc import RPCClient


def init_account(pk_name="accounts_pk"):
    def wrapper(func):
        def decorator(self, request, *args, **kwargs):
            account_pk = self.kwargs.get(pk_name)

            try:
                account = Account.objects.get(pk=account_pk)
            except Account.DoesNotExist:
                raise NotFound("Could not found account: {}".format(account_pk))

            if account.owner != self.request.user:
                raise PermissionDenied("You are not owner of this account.")

            request.account = account
            return func(self, request, *args, **kwargs)

        return decorator

    return wrapper


class AccountViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return self.request.user.accounts.all()

    @init_account(pk_name="pk")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save(owner=self.request.user)


class AddressViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.request.user.accounts.all()

    def get_password(self, user):
        salt = settings.SECRET_KEY.encode()
        password = user.password.encode()
        dk = hashlib.pbkdf2_hmac('sha256', password=password, salt=salt, iterations=100000)
        return binascii.hexlify(dk).decode()

    @init_account()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @init_account()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @init_account()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @list_route()
    def send(self):
        password = self.get_password(self.request.user)
        
    def perform_create(self, serializer):
        with transaction.atomic():
            client = RPCClient('docker.ethnode', 8545)

            password = self.get_password(self.request.user)
            address = client.personal_newAccount(password=password)
            serializer.save(account=self.request.account, address=address)
