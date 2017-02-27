class MC2PError(Exception):

    def __init__(self, message=None, json_body=None, resource=None, resource_id=None):
        super(MC2PError, self).__init__(message)

        self._message = message
        self.json_body = json_body
        self.resource = resource
        self.resource_id = resource_id


class InvalidRequestError(MC2PError):
    pass


class PermissionError(MC2PError):
    pass


class BadUseError(MC2PError):
    pass
