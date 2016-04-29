__author__ = 'andrew.shvv@gmail.com'

from django.conf.urls import url, include
from rest_framework_nested import routers

from ethclient.views import AccountViewSet, AddressViewSet

router = routers.SimpleRouter()
router.register(prefix=r'accounts', viewset=AccountViewSet, base_name="Account")

accounts_router = routers.NestedSimpleRouter(router, "accounts", lookup="accounts")
accounts_router.register(r"addresses", AddressViewSet, base_name='Address')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(accounts_router.urls)),
]
