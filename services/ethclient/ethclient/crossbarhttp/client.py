import base64
import datetime
import hashlib
import hmac
import json
from random import randint
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class ClientBaseException(Exception):
    """
    Catch all Exception for this class
    """
    pass


class ClientNoCalleeRegistered(ClientBaseException):
    """
    Exception thrown when no callee was registered
    """
    pass


class ClientBadUrl(ClientBaseException):
    """
    Exception thrown when the URL is invalid
    """
    pass


class ClientBadHost(ClientBaseException):
    """
    Exception thrown when the host name is invalid
    """
    pass


class ClientMissingParams(ClientBaseException):
    """
    Exception thrown when the request is missing params
    """
    pass


class ClientSignatureError(ClientBaseException):
    """
    Exception thrown when the signature check fails (if server has "key" and "secret" set)
    """
    pass


class ClientCallRuntimeError(ClientBaseException):
    """
    Exception thrown when a call generated an exception
    """
    pass


class Client(object):
    def __init__(self, url, key=None, secret=None, verbose=False):
        """
        Creates a client to connect to the HTTP bridge services
        :param url: The URL to connect to to access the Crossbar
        :param key: The key for the API calls
        :param secret: The secret for the API calls
        :param verbose: True if you want debug messages printed
        :return: Nothing
        """
        assert url is not None

        self.url = url
        self.key = key
        self.secret = secret
        self.verbose = verbose
        self.sequence = 1

    def publish(self, topic, *args, **kwargs):
        """
        Publishes the request to the bridge service
        :param topic: The topic to publish to
        :param args: The arguments
        :param kwargs: The key/word arguments
        :return: The ID of the publish
        """
        assert topic is not None

        params = {
            "topic": topic,
            "args": args,
            "kwargs": kwargs
        }

        response = self._make_api_call("POST", self.url, json_params=params)
        return response["id"]

    def call(self, procedure, *args, **kwargs):
        """
        Calls a procedure from the bridge service
        :param topic: The topic to publish to
        :param args: The arguments
        :param kwargs: The key/word arguments
        :return: The response from calling the procedure
        """
        assert procedure is not None

        params = {
            "procedure": procedure,
            "args": args,
            "kwargs": kwargs
        }

        response = self._make_api_call("POST", self.url, json_params=params)

        value = None
        if "args" in response and len(response["args"]) > 0:
            value = response["args"][0]

        if "error" in response:
            error = response["error"]
            if "wamp.error.no_such_procedure" in error:
                raise ClientNoCalleeRegistered(value)
            else:
                raise ClientCallRuntimeError(value)

        return value

    def _compute_signature(self, body):
        """
        Computes the signature.

        Described at:
        http://crossbar.io/docs/HTTP-Bridge-Services-Caller/

        Reference code is at:
        https://github.com/crossbario/crossbar/blob/master/crossbar/adapter/rest/common.py

        :return: (signature, none, timestamp)
        """

        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        nonce = randint(0, 2 ** 53)

        # Compute signature: HMAC[SHA256]_{secret} (key | timestamp | seq | nonce | body) => signature
        hm = hmac.new(self.secret, None, hashlib.sha256)
        hm.update(self.key)
        hm.update(timestamp)
        hm.update(str(self.sequence))
        hm.update(str(nonce))
        hm.update(body)
        signature = base64.urlsafe_b64encode(hm.digest())

        return signature, nonce, timestamp

    def _make_api_call(self, method, url, json_params=None):
        """
        Performs the REST API Call
        :param method: HTTP Method
        :param url:  The URL
        :param json_params: The parameters intended to be JSON serialized
        :return:
        """
        if self.verbose is True:
            print("\ncrossbarhttp: Request: %s %s" % (method, url))

        if json_params is not None:
            encoded_params = json.dumps(json_params)
            encoded_params = encoded_params.encode()
            headers = {'Content-Type': 'application/json'}
        else:
            encoded_params = None
            headers = {}

        if encoded_params is not None and self.verbose is True:
            print("crossbarhttp: Params: " + encoded_params)

        if self.key is not None and self.secret is not None and encoded_params is not None:
            signature, nonce, timestamp = self._compute_signature(encoded_params)
            params = urlencode({
                "timestamp": timestamp,
                "seq": str(self.sequence),
                "nonce": nonce,
                "signature": signature,
                "key": self.key
            })
            if self.verbose is True:
                print("crossbarhttp: Signature Params: " + params)
            url += "?" + params

        # TODO: I can't figure out what this is.  Guessing it is a number you increment on every call
        self.sequence += 1

        try:
            request = Request(url, data=encoded_params, headers=headers)
            request.get_method = lambda: method
            response = urlopen(request).read().decode()
            if self.verbose is True:
                print("crossbarhttp: Response: " + response)

            return json.loads(response)


        except HTTPError as e:
            if e.code == 400:
                raise ClientMissingParams(str(e))
            elif e.code == 401:
                raise ClientSignatureError(str(e))
            else:
                raise ClientBadUrl(str(e))
        except URLError as e:
            raise ClientBadHost(str(e))


from django.conf import settings

_client = None


def get_crossbar_client(*args, **kwargs):
    url = settings.ROUTER_URL

    global _client
    if _client is None:
        _client = Client(url, *args, **kwargs)
    return _client


def set_crossbar_client(client):
    global _client
    _client = client
