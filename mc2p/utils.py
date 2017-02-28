from .errors import BadUseError


def id_required_and_not_deleted(func):
    """
    Decorator to check if the json_dict have an id and
    the object was not deleted
    :param func: function to decorate
    :return: function decorated
    """
    def result(self, *args, **kwargs):
        if not self.json_dict.get(self.ID_PROPERTY):
            raise BadUseError('Object don\'t have ID')
        if self._deleted:
            raise BadUseError('Object deleted')
        return func(self, *args, **kwargs)
    return result
