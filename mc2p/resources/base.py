import requests


class APIRequest:
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

    def _request(self, method):
        def func(url, data=None):
            return requests.request(
                method,
                self.get_abs_url(url),
                data=data,
                headers=self.headers
            ).json()

        return func


def is_valid_action(action):
    def decorator(func):
        def result(self, *args, **kwargs):
            if action not in self.VALID_ACTIONS:
                raise Exception('Invalid action for this resource')
            return func(self, *args, **kwargs)
        return result
    return decorator


class Resource:
    URL = '/resource/'
    VALID_ACTIONS = ['create', 'list', 'detail', 'change', 'delete']

    def __init__(self, api_request):
        self.api_request = api_request

    def detail_url(self, resource_id):
        return '%s%s/' % (
            self.URL,
            resource_id
        )

    @is_valid_action('create')
    def create(self, data):
        return self.api_request.post(
            self.URL,
            data
        )

    @is_valid_action('list')
    def list(self):
        return self.api_request.get(self.URL)

    @is_valid_action('detail')
    def detail(self, resource_id):
        return self.api_request.get(
            self.detail_url(resource_id)
        )

    @is_valid_action('change')
    def change(self, resource_id, data):
        return self.api_request.patch(
            self.detail_url(resource_id),
            data
        )

    @is_valid_action('delete')
    def delete(self, resource_id):
        return self.api_request.delete(
            self.detail_url(resource_id)
        )


class ReadOnlyResource(Resource):
    VALID_ACTIONS = ['list', 'detail']


class CreateReadOnlyResource(Resource):
    VALID_ACTIONS = ['create', 'list', 'detail']
