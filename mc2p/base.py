from .utils import is_valid_action, id_required_and_not_deleted


class Paginator(object):
    def __init__(self, json_dict, object_item_class, resource):
        self.count = json_dict.get('count', 0)
        self._previous = json_dict.get('previous', None)
        self._next = json_dict.get('next', None)
        self.results = [
            object_item_class(result, resource) for result in json_dict.get('results', [])
        ]
        self.resource = resource

    def get_next_list(self):
        if self._next:
            return self.resource.list(abs_url=self._next)
        return None

    def get_previous_list(self):
        if self._previous:
            return self.resource.list(abs_url=self._previous)
        return None


class ObjectItem(object):
    ID_PROPERTY = 'id'
    VALID_ACTIONS = ['create', 'retrieve', 'save', 'delete']

    def __init__(self, json_dict, resource):
        if json_dict is None:
            json_dict = {}
        self.json_dict = json_dict

        self.resource = resource

        self._deleted = False

    def __getattr__(self, key):
        return self.json_dict[key]

    def __setattr__(self, key, value):
        if key in ['json_dict', 'resource', '_deleted']:
            super(ObjectItem, self).__setattr__(key, value)
        else:
            self.json_dict[key] = value

    @is_valid_action('create')
    def _create(self):
        obj = self.resource.create(
            self.json_dict
        )
        self.json_dict = obj.json_dict

    @id_required_and_not_deleted
    @is_valid_action('save')
    def _change(self):
        obj = self.resource.change(
            self.json_dict[self.ID_PROPERTY],
            self.json_dict
        )
        self.json_dict = obj.json_dict

    @is_valid_action('retrieve')
    def retrieve(self):
        obj = self.resource.detail(
            self.json_dict[self.ID_PROPERTY]
        )
        self.json_dict = obj.json_dict

    def save(self):
        if self.json_dict.get(self.ID_PROPERTY, False):
            self._change()
        else:
            self._create()

    @id_required_and_not_deleted
    @is_valid_action('delete')
    def delete(self):
        self.resource.delete(
            self.json_dict[self.ID_PROPERTY]
        )
        self._deleted = True


class ReadOnlyObjectItem(ObjectItem):
    VALID_ACTIONS = ['retrieve']


class CreateReadOnlyObjectItem(ObjectItem):
    VALID_ACTIONS = ['create', 'retrieve']


class Resource(object):
    URL = '/resource/'
    VALID_ACTIONS = ['create', 'list', 'detail', 'change', 'delete']
    OBJECT_ITEM_CLASS = None

    def __init__(self, api_request):
        self.api_request = api_request

    def detail_url(self, resource_id):
        return '%s%s/' % (
            self.URL,
            resource_id
        )

    def _one_item(self, func, data=None, resource_id=None):
        if not resource_id:
            url = self.URL
        else:
            url = self.detail_url(resource_id)

        return self.OBJECT_ITEM_CLASS(
            func(
                url,
                data,
                resource=self,
                resource_id=resource_id
            ),
            self
        )

    @is_valid_action('create')
    def create(self, data):
        return self._one_item(self.api_request.post, data=data)

    @is_valid_action('list')
    def list(self, abs_url=None):
        if abs_url:
            json_dict = self.api_request.get(
                abs_url=abs_url,
                resource=self
            )
        else:
            json_dict = self.api_request.get(
                self.URL,
                resource=self
            )
        return Paginator(
            json_dict,
            self.OBJECT_ITEM_CLASS,
            self
        )

    @is_valid_action('detail')
    def detail(self, resource_id):
        return self._one_item(self.api_request.get, resource_id=resource_id)

    @is_valid_action('change')
    def change(self, resource_id, data):
        return self._one_item(self.api_request.patch, data=data, resource_id=resource_id)

    @is_valid_action('delete')
    def delete(self, resource_id):
        self._one_item(self.api_request.delete, resource_id=resource_id)


class ReadOnlyResource(Resource):
    VALID_ACTIONS = ['list', 'detail']


class CreateReadOnlyResource(Resource):
    VALID_ACTIONS = ['create', 'list', 'detail']
