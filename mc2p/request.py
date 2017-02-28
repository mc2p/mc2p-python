from .errors import InvalidRequestError

import json
import requests


class APIRequest(object):
    """
    API request - class used to connect with the API
    """
    AUTHORIZATION_HEADER = 'AppKeys'
    API_URL = 'api.mychoice2pay.com'

    def __init__(self, key, secret_key):
        """
        Initializes an api request
        :param key: key to connect with API
        :param secret_key: secret key to connect with API
        """
        self.key = key
        self.secret_key = secret_key

        self.post = self._request('POST', 201)
        self.get = self._request('GET')
        self.patch = self._request('PATCH')
        self.delete = self._request('DELETE', 204)

    @property
    def headers(self):
        """
        Creates the headers to include in the request
        :return: A dictionary with the headers needed for the API
        """
        return {
            'authorization': '%s %s:%s' % (
                self.AUTHORIZATION_HEADER,
                self.key,
                self.secret_key
            ),
            'content-type': 'application/json'
        }

    def get_abs_url(self, url):
        """
        :param url: relative url
        :return: The absolute url to send the request
        """
        return 'https://%s%s' % (
            self.API_URL,
            url
        )

    def _request(self, method, status_code=200):
        """
        Decorator to make the request based on the method received
        :param method: method to make the request
        :param status_code: value to check if the request receive a correct response
        :return: a function to make the request
        """
        def func(rel_url=None, data=None, abs_url=None, resource=None, resource_id=None):
            request = requests.request(
                method,
                abs_url if abs_url else self.get_abs_url(rel_url),
                data=json.dumps(data),
                headers=self.headers
            )

            if request.status_code != status_code:
                raise InvalidRequestError(
                    'Error %s' % request.status_code,
                    json_body=request.json(),
                    resource=resource,
                    resource_id=resource_id
                )

            if status_code == 204:
                return {}
            return request.json()
        return func
