__author__ = 'andrew.shvv@gmail.com'

from celery.task import Task
from django.db import connection
from mock import patch

from core.utils.logging import getPrettyLogger

logger = getPrettyLogger(__name__)


class CeleryMockMixin():
    """
        CeleryMockMixin substitute original DBTask in order to close db connections
    """

    def __init__(self):
        # WARNING!: Be careful with names you may override variables in the class that inherit this mixin!
        self._celery_patcher = None

    def mock_celery(self):
        self._celery_patcher = patch('ethclient.celery.base.DBTask', new=DBTask)
        self.mock_dbtask = self._celery_patcher.start()

    def unmock_celery(self):
        self._celery_patcher.stop()


class DBTask(Task):
    abstract = True

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        connection.close()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        connection.close()

    def on_success(self, retval, task_id, args, kwargs):
        connection.close()
