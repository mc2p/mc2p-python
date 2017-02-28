from .mixin import ObjectItemMixin, DeleteObjectItemMixin, RetrieveObjectItemMixin, SaveObjectItemMixin, \
    CreateObjectItemMixin, ResourceMixin, ListDetailResourceMixin, CreateResourceMixin, DeleteResourceMixin, \
    ChangeResourceMixin


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


class ObjectItem(ObjectItemMixin):
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


class RetrieveObjectItem(RetrieveObjectItemMixin, ObjectItem):
    pass


class CreateRetrieveObjectItem(CreateObjectItemMixin, ObjectItem):
    pass


class SaveRetrieveObjectItem(SaveObjectItemMixin, RetrieveObjectItem):
    pass


class DeleteSaveRetrieveObjectItem(DeleteObjectItemMixin, SaveRetrieveObjectItem):
    pass


class Resource(ResourceMixin):
    PAGINATOR_CLASS = Paginator

    def __init__(self, api_request):
        self.api_request = api_request


class ListDetailResource(ListDetailResourceMixin, Resource):
    pass


class CreateListDetailResource(CreateResourceMixin, ListDetailResource):
    pass


class DeleteChangeCreateListDetailResource(DeleteResourceMixin, ChangeResourceMixin, CreateListDetailResource):
    pass
