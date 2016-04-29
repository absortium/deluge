__author__ = 'andrew.shvv@gmail.com'

from celery import Task

from core.utils.logging import getPrettyLogger

logger = getPrettyLogger(__name__)


class DBTask(Task):
    """
        Now this class mainly is using in test as mock endpoint.
    """
    abstract = True

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        pass
        # connection.close()

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        pass
        # connection.close()

    def on_success(self, retval, task_id, args, kwargs):
        pass
        # connection.close()


def get_base_class():
    return DBTask
