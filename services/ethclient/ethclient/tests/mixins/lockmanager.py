__author__ = 'andrew.shvv@gmail.com'

from mock import patch, Mock

from core.utils.logging import getLogger

logger = getLogger(__name__)


class LockManagerMockMixin():
    """
        LockManagerMockMixin substitute original lock manager and always return lock.
    """

    def __init__(self):
        # WARNING!: Be careful with names you may override variables in the class that inherit this mixin!
        self._lockmanager_patcher = None

    def mock_lockmanager(self):
        manager = MockLockManager()
        self._lockmanager_patcher = patch('ethclient.lockmanager.LockManager', new=manager)
        self._lockmanager_patcher.start()

    def unmock_lockmanager(self):
        self._lockmanager_patcher.stop()


class MockLockManager(Mock):
    topics = {}

    def __init__(self, *args, **kwargs):
        # self.mock_lock = object()
        super().__init__(*args, **kwargs)

    def lock(self, account_pk):
        return object()

    def unlock(self, lock):
        pass
