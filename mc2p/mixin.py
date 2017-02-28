from .utils import id_required_and_not_deleted


class ObjectItemMixin(object):
    ID_PROPERTY = 'id'
    json_dict = None
    resource = None
    _deleted = False


class DeleteObjectItemMixin(ObjectItemMixin):
    @id_required_and_not_deleted
    def delete(self):
        self.resource.delete(
            self.json_dict[self.ID_PROPERTY]
        )
        self._deleted = True


class RetrieveObjectItemMixin(ObjectItemMixin):
    @id_required_and_not_deleted
    def retrieve(self):
        obj = self.resource.detail(
            self.json_dict[self.ID_PROPERTY]
        )
        self.json_dict = obj.json_dict


class CreateObjectItemMixin(ObjectItemMixin):
    def _create(self):
        obj = self.resource.create(
            self.json_dict
        )
        self.json_dict = obj.json_dict

    def save(self):
        if not self.json_dict.get(self.ID_PROPERTY, False):
            self._create()


class SaveObjectItemMixin(CreateObjectItemMixin):
    @id_required_and_not_deleted
    def _change(self):
        obj = self.resource.change(
            self.json_dict[self.ID_PROPERTY],
            self.json_dict
        )
        self.json_dict = obj.json_dict

    def save(self):
        if self.json_dict.get(self.ID_PROPERTY, False):
            self._change()
        else:
            self._create()


class ResourceMixin(object):
    URL = '/resource/'
    OBJECT_ITEM_CLASS = None
    PAGINATOR_CLASS = None
    api_request = None

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


class ListDetailResourceMixin(ResourceMixin):
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

        return self.PAGINATOR_CLASS(
            json_dict,
            self.OBJECT_ITEM_CLASS,
            self
        )

    def detail(self, resource_id):
        return self._one_item(self.api_request.get,
                              resource_id=resource_id)


class CreateResourceMixin(ResourceMixin):
    def create(self, data):
        return self._one_item(self.api_request.post,
                              data=data)


class ChangeResourceMixin(ResourceMixin):
    def change(self, resource_id, data):
        return self._one_item(self.api_request.patch,
                              data=data,
                              resource_id=resource_id)


class DeleteResourceMixin(ResourceMixin):
    def delete(self, resource_id):
        self._one_item(self.api_request.delete,
                       resource_id=resource_id)