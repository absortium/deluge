__author__ = 'andrew.shvv@gmail.com'

from celery.utils.log import get_task_logger
from django.db import models, connection

celery_logger = get_task_logger(__name__)


class LockingManager(models.Manager):
    """ Add lock/unlock functionality to manager.
        Origin: http://stackoverflow.com/questions/19686204/django-orm-and-locking-table

    Example::

        class Job(models.Model):

            manager = LockingManager()

            counter = models.IntegerField(null=True, default=0)

            @staticmethod
            def do_atomic_update(job_id)
                ''' Updates job integer, keeping it below 5 '''
                try:
                    # Ensure only one HTTP request can do this update at once.
                    Job.objects.lock()

                    job = Job.object.get(id=job_id)
                    # If we don't lock the tables two simultanous
                    # requests might both increase the counter
                    # going over 5
                    if job.counter < 5:
                        job.counter += 1
                        job.save()

                finally:
                    Job.objects.unlock()


    """

    def lock(self):
        """ Lock table.

        Locks the object model table so that atomic update is possible.
        Simulatenous database access request pend until the lock is unlock()'ed.

        Note: If you need to lock multiple tables, you need to do lock them
        all in one SQL clause and this function is not enough. To avoid
        dead lock, all tables must be locked in the same order.

        See http://dev.mysql.com/doc/refman/5.0/en/lock-tables.html
        """
        cursor = connection.cursor()
        table = self.model._meta.db_table
        cursor.execute("LOCK TABLES %s WRITE" % table)
        row = cursor.fetchone()
        return row

    def unlock(self):
        """ Unlock the table. """
        cursor = connection.cursor()
        table = self.model._meta.db_table
        cursor.execute("UNLOCK TABLES")
        row = cursor.fetchone()
        return row


_lock_manager = None


def get_lock_manager():
    global _lock_manager
    if not _lock_manager:
        _lock_manager = LockingManager()
    return _lock_manager
