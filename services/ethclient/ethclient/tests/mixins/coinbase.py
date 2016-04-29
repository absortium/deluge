__author__ = 'andrew.shvv@gmail.com'

from mock import patch

from core.utils.logging import getLogger

logger = getLogger(__name__)

address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"


class CoinbaseMockMixin():
    """
        CoinbaseMockMixin substitute original coinbase client and return mock btc/eth addresses
    """

    def __init__(self):
        # WARNING!: Be careful with names you may override variables in the class that inherit this mixin!
        self._coinbase_patcher = None

    def mock_coinbase(self):
        self._coinbase_patcher = patch('ethclient.wallet.bitcoin.BitcoinClient.create_address', return_value=address)
        self.mock_client = self._coinbase_patcher.start()

    def unmock_coinbase(self):
        self._coinbase_patcher.stop()
