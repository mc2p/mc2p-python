from .errors import BadUseError, PermissionError


def is_valid_action(action):
    def decorator(func):
        def result(self, *args, **kwargs):
            if action not in self.VALID_ACTIONS:
                raise PermissionError('Invalid action')
            return func(self, *args, **kwargs)
        return result
    return decorator


def id_required_and_not_deleted(func):
    def result(self, *args, **kwargs):
        if not self.json_dict.get(self.ID_PROPERTY):
            raise BadUseError('Object don\'t have ID')
        if self._deleted:
            raise BadUseError('Object deleted')
        return func(self, *args, **kwargs)
    return result
