from .errors import InvalidRequestError

import requests


class APIRequest(object):
    AUTHORIZATION_HEADER = 'AppKeys'
    API_URL = 'api.mychoice2pay.com'

    def __init__(self, key, secret_key):
        self.key = key
        self.secret_key = secret_key

        self.post = self._request('POST')
        self.get = self._request('GET')
        self.patch = self._request('PATCH')
        self.delete = self._request('DELETE')

    @property
    def headers(self):
        return {
            'authorization': '%s %s:%s' % (
                self.AUTHORIZATION_HEADER,
                self.key,
                self.secret_key
            )
        }

    def get_abs_url(self, url):
        return 'https://%s%s' % (
            self.API_URL,
            url
        )

    def _request(self, method, status_code=200):
        def func(rel_url=None, data=None, abs_url=None, resource=None, resource_id=None):
            request = requests.request(
                method,
                abs_url if abs_url else self.get_abs_url(rel_url),
                data=data,
                headers=self.headers
            )

            if request.status_code != status_code:
                raise InvalidRequestError(
                    'Error %s' % request.status_code,
                    json_body=request.json(),
                    resource=resource,
                    resource_id=resource_id
                )
            return request.json()
        return func
