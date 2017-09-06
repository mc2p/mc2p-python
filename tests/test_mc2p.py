import unittest
import warnings

try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser

import mc2p
from mc2p import objects, resources, base

if hasattr(unittest, 'mock'):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock


class TestMC2P(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.readfp(open('config.example.ini'))

        key = config.get('mc2p', 'key')
        secret_key = config.get('mc2p', 'secret_key')

        self.client = mc2p.MC2PClient(key, secret_key)

    def test_defaults_init(self):
        client = mc2p.MC2PClient('key', 'secret_key')
        self.assertEqual('key', client.api_request.key)
        self.assertEqual('secret_key', client.api_request.secret_key)

    def test_product(self):
        product_list = self.client.product.list()
        self.assertIsInstance(product_list, base.Paginator)
        self.assertIsInstance(product_list.results, list)
        self.assertIsInstance(product_list.count, int)
