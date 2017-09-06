from .mixin import ObjectItemMixin, DeleteObjectItemMixin, RetrieveObjectItemMixin, SaveObjectItemMixin, \
    CreateObjectItemMixin, ResourceMixin, DetailOnlyResourceMixin, ReadOnlyResourceMixin, CreateResourceMixin, \
    DeleteResourceMixin, ChangeResourceMixin


class Paginator(object):
    """
    Paginator - class used on list requests
    """
    def __init__(self, json_dict, object_item_class, resource):
        """
        Initializes a paginator
        :param json_dict: Response from server
        :param object_item_class: Class to wrapper all the items from results field
        :param resource: Resource used to get next and previous items
        """
        self.count = json_dict.get('count', 0)
        self._previous = json_dict.get('previous', None)
        self._next = json_dict.get('next', None)
        self.results = [
            object_item_class(result, resource) for result in json_dict.get('results', [])
        ]
        self.resource = resource

    def get_next_list(self):
        """
        :return: Paginator object with the next items
        """
        if self._next:
            return self.resource.list(abs_url=self._next)
        return None

    def get_previous_list(self):
        """
        :return: Paginator object with the previous items
        """
        if self._previous:
            return self.resource.list(abs_url=self._previous)
        return None


class ObjectItem(ObjectItemMixin):
    """
    Object item - class used to wrap the data from API that represent an item
    """
    def __init__(self, json_dict, resource):
        """
        Initializes an object item
        :param json_dict: Data of the object
        :param resource: Resource used to delete, save, create or retrieve the object
        """
        if json_dict is None:
            json_dict = {}
        self.json_dict = json_dict

        self.resource = resource

        self._deleted = False

    def __getattr__(self, key):
        """
        Allows use the following syntax to get a field of the object:
          obj.name
        :param key: Field to return
        :return: Value of the field from json_dict
        """
        return self.json_dict[key]

    def __setattr__(self, key, value):
        """
        Allows use the following syntax to set a field of the object:
          obj.name = 'example'
        :param key: Field to change
        :param value: Content to replace the current value
        """
        if key in ['json_dict', 'resource', '_deleted']:
            super(ObjectItem, self).__setattr__(key, value)
        else:
            self.json_dict[key] = value


class ReadOnlyObjectItem(RetrieveObjectItemMixin, ObjectItem):
    """
    Object item that allows retrieve an item
    """
    @classmethod
    def get(cls, object_id):
        """
        Retrieve object with object_id and return
        :param object_id: Id to retrieve
        :return: Object after retrieve
        """
        obj = cls({
            cls.ID_PROPERTY: object_id
        }, cls.resource)
        obj.retrieve()
        return obj


class CRObjectItem(CreateObjectItemMixin, ReadOnlyObjectItem):
    """
    Object item that allows retrieve and create an item
    """
    pass


class CRUObjectItem(SaveObjectItemMixin, ReadOnlyObjectItem):
    """
    Object item that allows retrieve, create and change an item
    """
    pass


class CRUDObjectItem(DeleteObjectItemMixin, CRUObjectItem):
    """
    Object item that allows retrieve, create, change and delete an item
    """
    pass


class Resource(ResourceMixin):
    """
    Resource - class used to manage the requests to the API related with a resource
    ex: product
    """
    PAGINATOR_CLASS = Paginator

    def __init__(self, api_request):
        """
        Initializes a resource
        :param api_request: Api request used to make all the requests to the API
        """
        self.api_request = api_request


class DetailOnlyResource(DetailOnlyResourceMixin, Resource):
    """
    Resource that allows send requests of detail
    """
    pass


class ReadOnlyResource(ReadOnlyResourceMixin, Resource):
    """
    Resource that allows send requests of list and detail
    """
    pass


class CRResource(CreateResourceMixin, ReadOnlyResource):
    """
    Resource that allows send requests of create, list and detail
    """
    pass


class CRUDResource(DeleteResourceMixin, ChangeResourceMixin, CRResource):
    """
    Resource that allows send requests of delete, change, create, list and detail
    """
    pass
