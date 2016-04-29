__author__ = 'andrew.shvv@gmail.com'

import six
from rest_framework.exceptions import APIException, _force_text_recursive
from rest_framework.status import HTTP_409_CONFLICT


class AlreadyExistError(APIException):
    status_code = HTTP_409_CONFLICT

    def __init__(self, detail):
        # The details should always be coerced to a list if not already.
        if not isinstance(detail, dict) and not isinstance(detail, list):
            detail = [detail]
        self.detail = _force_text_recursive(detail)

    def __str__(self):
        return six.text_type(self.detail)
