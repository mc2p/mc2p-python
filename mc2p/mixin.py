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


class ChargeObjectItemMixin(ObjectItemMixin):
    """
    Allows make charge an object item
    """
    @id_required_and_not_deleted
    def charge(self, data=None):
        """
        Charge the object item
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.charge(
            self.json_dict[self.ID_PROPERTY],
            data
        )


class RefundCaptureVoidObjectItemMixin(ObjectItemMixin):
    """
    Allows make refund, capture and void an object item
    """
    @id_required_and_not_deleted
    def refund(self, data=None):
        """
        Refund the object item
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.refund(
            self.json_dict[self.ID_PROPERTY],
            data
        )

    @id_required_and_not_deleted
    def capture(self, data=None):
        """
        Capture the object item
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.capture(
            self.json_dict[self.ID_PROPERTY],
            data
        )

    @id_required_and_not_deleted
    def void(self, data=None):
        """
        Void the object item
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.void(
            self.json_dict[self.ID_PROPERTY],
            data
        )


class CardShareObjectItemMixin(ObjectItemMixin):
    """
    Allows make card and share an object item
    """
    @id_required_and_not_deleted
    def card(self, gateway_code, data=None):
        """
        Send card details
        :param gateway_code: gateway_code to send
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.card(
            self.json_dict[self.ID_PROPERTY],
            gateway_code,
            data
        )

    @id_required_and_not_deleted
    def share(self, data=None):
        """
        Send share details
        :param data: data to send
        :return: response dictionary
        """
        return self.resource.share(
            self.json_dict[self.ID_PROPERTY],
            data
        )


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


class DetailOnlyResourceMixin(ResourceMixin):
    """
    Allows send requests of detail
    """
    def detail(self, resource_id):
        """
        :param resource_id: id to request
        :return: an object item class with the response of the server
        """
        return self._one_item(self.api_request.get,
                              resource_id=resource_id)


class ReadOnlyResourceMixin(DetailOnlyResourceMixin):
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


class ActionsResourceMixin(ResourceMixin):
    """
    Allows send requests of actions
    """
    def detail_action_url(self, resource_id, action):
        """
        :param resource_id: id used on the url returned
        :param action: action used on the url returned
        :return: url to make an action in an item
        """
        return '%s%s/%s/' % (
            self.PATH,
            resource_id,
            action
        )

    def _one_item_action(self, func, resource_id, action, data=None):
        """
        Help function to make an action in an item
        :param func: function to make the request
        :param resource_id: id to use on the requested url
        :param action: action to use on the requested url
        :param data: data passed in the request
        :return: response dictionary
        """
        url = self.detail_action_url(resource_id, action)

        return func(
            url,
            data,
            resource=self,
            resource_id=resource_id
        )


class ChargeResourceMixin(ActionsResourceMixin):
    """
    Allows send action requests of charge
    """
    def charge(self, resource_id, data=None):
        """
        :param resource_id: id to request
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post_200,
                                     resource_id,
                                     'charge',
                                     data)


class RefundCaptureVoidResourceMixin(ActionsResourceMixin):
    """
    Allows send action requests of refund, capture and void
    """
    def refund(self, resource_id, data=None):
        """
        :param resource_id: id to request
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post_200,
                                     resource_id,
                                     'refund',
                                     data)

    def capture(self, resource_id, data=None):
        """
        :param resource_id: id to request
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post_200,
                                     resource_id,
                                     'capture',
                                     data)

    def void(self, resource_id, data=None):
        """
        :param resource_id: id to request
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post_200,
                                     resource_id,
                                     'void',
                                     data)


class CardShareResourceMixin(ActionsResourceMixin):
    """
    Allows send action requests of card and share
    """
    def card(self, resource_id, gateway_code, data=None):
        """
        :param resource_id: id to request
        :param gateway_code: gateway_code to send
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post,
                                     resource_id,
                                     'card/%s' % gateway_code,
                                     data)

    def share(self, resource_id, data=None):
        """
        :param resource_id: id to request
        :param data: data to send
        :return: response dictionary
        """
        return self._one_item_action(self.api_request.post,
                                     resource_id,
                                     'share',
                                     data)
