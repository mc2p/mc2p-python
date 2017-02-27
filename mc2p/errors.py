import sys


class MC2PError(Exception):

    def __init__(self, message=None, json_body=None, resource=None, resource_id=None):
        super(MC2PError, self).__init__(message)

        self._message = message
        self.json_body = json_body
        self.resource = resource
        self.resource_id = resource_id

    def __unicode__(self):
        return u"Message: {0}, Body: {1}".format(self._message, self.json_body)

    if sys.version_info > (3, 0):
        def __str__(self):
            return self.__unicode__()
    else:
        def __str__(self):
            return unicode(self).encode('utf-8')


class InvalidRequestError(MC2PError):
    pass


class PermissionError(MC2PError):
    pass


class BadUseError(MC2PError):
    pass
