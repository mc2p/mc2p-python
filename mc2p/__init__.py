__title__ = 'MyChoice2Pay Python'
__version__ = '0.0.2'
__author__ = 'MyChoice2Pay'
__license__ = 'BSD 2-Clause'
__copyright__ = 'Copyright 2017 MyChoice2Pay'

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'


from .mc2p import MC2PClient
