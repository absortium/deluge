__author__ = "andrew.shvv@gmail.com"

from ethclient.crossbarhttp import publishment
from ethclient.crossbarhttp.client import get_crossbar_client
from ethclient.tests.base import EthClientUnitTest
from core.utils.logging import getLogger

logger = getLogger(__name__)


class PublishmentsTest(EthClientUnitTest):
    def test_publishments_atmoic(self):
        """
            Check publishemnt.atomic context manager. If exception was raised inside the block
            than publishments should not be published.
        """

        try:
            with publishment.atomic():
                client = get_crossbar_client()
                client.publish("sometopic", text="sometext")

                raise Exception("Something wrong!")
        except Exception:
            pass

        self.assertEqual(self.get_publishments("sometopic"), None)
