import sys

from .utils import id_required_and_not_deleted


class ObjectItemMixin(object):
    """
    Basic info of the object item
    """
    ID_PROPERTY = 'id'
    json_dict = None
    resource = None
    _deleted = False

    def __unicode__(self):
        """
        :return: Name of the object and content
        """
        return u"{0} {1}".format(self.__class__.__name__, self.json_dict)

    if sys.version_info > (3, 0):
        def __str__(self):
            """
            Python >3
            :return: Unicode representation
            """
            return self.__unicode__()
    else:
        def __str__(self):
            """
            Python <3
            :return: Unicode representation
            """
            return unicode(self).encode('utf-8')

    def __repr__(self):
        """
        :return: Unicode representation
        """
        return self.__str__()


class DeleteObjectItemMixin(ObjectItemMixin):
    """
    Allows delete an object item
    """
    @id_required_and_not_deleted
    def delete(self):
        """
        Deletes the object item
        """
        self.resource.delete(
            self.json_dict[self.ID_PROPERTY]
        )
        self._deleted = True


class RetrieveObjectItemMixin(ObjectItemMixin):
    """
    Allows retrieve an object item
    """
    @id_required_and_not_deleted
    def retrieve(self):
        """
        Retrieves the data of the object item
        """
        obj = self.resource.detail(
            self.json_dict[self.ID_PROPERTY]
        )
        self.json_dict = obj.json_dict


class CreateObjectItemMixin(ObjectItemMixin):
    """
    Allows create an object item
    """
    def _create(self):
        """
        Creates the object item with the json_dict data
        """
        obj = self.resource.create(
            self.json_dict
        )
        self.json_dict = obj.json_dict

    def save(self):
        """
        Executes the internal function _create if the object item don't have id
        """
        if not self.json_dict.get(self.ID_PROPERTY, False):
            self._create()


class SaveObjectItemMixin(CreateObjectItemMixin):
    """
    Allows change an object item
    """
    @id_required_and_not_deleted
    def _change(self):
        """
        Changes the object item with the json_dict data
        """
        obj = self.resource.change(
            self.json_dict[self.ID_PROPERTY],
            self.json_dict
        )
        self.json_dict = obj.json_dict

    def save(self):
        """
        Executes the internal function _create if the object item don't have id,
        in other case, call to _change
        """
        if self.json_dict.get(self.ID_PROPERTY, False):
            self._change()
        else:
            self._create()


class PayURLMixin(ObjectItemMixin):
    """
    Add property to get pay_url based on token
    """
    PAY_URL = 'https://pay.mychoice2pay.com/#/%s'
    IFRAME_URL = 'https://pay.mychoice2pay.com/#/%s/iframe'

    @property
    @id_required_and_not_deleted
    def pay_url(self):
        """
        :return: pay url
        """
        return self.PAY_URL % self.json_dict['token']

    @property
    @id_required_and_not_deleted
    def iframe_url(self):
        """
        :return: iframe url
        """
        return self.IFRAME_URL % self.json_dict['token']


class ResourceMixin(object):
    """
    Basic info of the resource
    """
    PATH = '/resource/'
    OBJECT_ITEM_CLASS = None
    PAGINATOR_CLASS = None
    api_request = None

    def detail_url(self, resource_id):
        """
        :param resource_id: id used on the url returned
        :return: url to request or change an item
        """
        return '%s%s/' % (
            self.PATH,
            resource_id
        )

    def _one_item(self, func, data=None, resource_id=None):
        """
        Help function to make a request that return one item
        :param func: function to make the request
        :param data: data passed in the request
        :param resource_id: id to use on the requested url
        :return: an object item that represent the item returned
        """
        if not resource_id:
            url = self.PATH
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


class ReadOnlyResourceMixin(ResourceMixin):
    """
    Allows send requests of list and detail
    """
    def list(self, abs_url=None):
        """
        :param abs_url: if is passed the request is sent to this url
        :return: a paginator class with the response of the server
        """
        if abs_url:
            json_dict = self.api_request.get(
                abs_url=abs_url,
                resource=self
            )
        else:
            json_dict = self.api_request.get(
                self.PATH,
                resource=self
            )

        return self.PAGINATOR_CLASS(
            json_dict,
            self.OBJECT_ITEM_CLASS,
            self
        )

    def detail(self, resource_id):
        """
        :param resource_id: id to request
        :return: an object item class with the response of the server
        """
        return self._one_item(self.api_request.get,
                              resource_id=resource_id)


class CreateResourceMixin(ResourceMixin):
    """
    Allows send requests of create
    """
    def create(self, data):
        """
        :param data: data used on the request
        :return: an object item class with the response of the server
        """
        return self._one_item(self.api_request.post,
                              data=data)


class ChangeResourceMixin(ResourceMixin):
    """
    Allows send requests of change
    """
    def change(self, resource_id, data):
        """
        :param resource_id: id to request
        :param data: data used on the request
        :return: an object item class with the response of the server
        """
        return self._one_item(self.api_request.patch,
                              data=data,
                              resource_id=resource_id)


class DeleteResourceMixin(ResourceMixin):
    """
    Allows send requests of delete
    """
    def delete(self, resource_id):
        """
        :param resource_id: id to request
        """
        self._one_item(self.api_request.delete,
                       resource_id=resource_id)
