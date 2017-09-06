import unittest
import warnings

try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser

import mc2p
from mc2p import objects, resources, base, errors

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

        self.mc2p_client = mc2p.MC2PClient(key, secret_key)

    def test_defaults_init(self):
        client = mc2p.MC2PClient('key', 'secret_key')
        self.assertEqual('key', client.api_request.key)
        self.assertEqual('secret_key', client.api_request.secret_key)

    def test_product(self):
        product_list = self.mc2p_client.product.list()
        self.assertIsInstance(product_list, base.Paginator)
        self.assertIsInstance(product_list.results, list)
        self.assertIsInstance(product_list.count, int)

        product = self.mc2p_client.Product({
            'name': 'Product 1',
            'price': 5.1,
            'description': 'Description Product 1'
        })
        product.save()
        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(float(product.price), 5.1)
        self.assertEqual(product.description, 'Description Product 1')

        product.name = 'Product 2'
        product.price = 5.2
        product.description = 'Description Product 2'
        product.save()
        self.assertEqual(product.name, 'Product 2')
        self.assertEqual(float(product.price), 5.2)
        self.assertEqual(product.description, 'Description Product 2')

        product_get = self.mc2p_client.Product.get(product.id)
        self.assertEqual(product_get.id, product.id)
        self.assertEqual(product_get.name, 'Product 2')
        self.assertEqual(float(product_get.price), 5.2)
        self.assertEqual(product_get.description, 'Description Product 2')

        product_get.delete()
        self.assertEqual(product_get._deleted, True)

        try:
            self.mc2p_client.Product.get(product.id)
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)

    def test_plan(self):
        plan_list = self.mc2p_client.plan.list()
        self.assertIsInstance(plan_list, base.Paginator)
        self.assertIsInstance(plan_list.results, list)
        self.assertIsInstance(plan_list.count, int)

        plan = self.mc2p_client.Plan({
            'name': 'Plan 1',
            'price': 5.1,
            'description': 'Description Plan 1',
            'duration': 1,
            'unit': 'M',
            'recurring': True
        })
        plan.save()
        self.assertEqual(plan.name, 'Plan 1')
        self.assertEqual(float(plan.price), 5.1)
        self.assertEqual(plan.description, 'Description Plan 1')
        self.assertEqual(plan.duration, 1)
        self.assertEqual(plan.unit, 'M')
        self.assertEqual(plan.recurring, True)

        plan.name = 'Plan 2'
        plan.price = 5.2
        plan.description = 'Description Plan 2'
        plan.duration = 2
        plan.unit = 'Y'
        plan.recurring = False
        plan.save()
        self.assertEqual(plan.name, 'Plan 2')
        self.assertEqual(float(plan.price), 5.2)
        self.assertEqual(plan.description, 'Description Plan 2')
        self.assertEqual(plan.duration, 2)
        self.assertEqual(plan.unit, 'Y')
        self.assertEqual(plan.recurring, False)

        plan_get = self.mc2p_client.Plan.get(plan.id)
        self.assertEqual(plan_get.id, plan.id)
        self.assertEqual(plan_get.name, 'Plan 2')
        self.assertEqual(float(plan_get.price), 5.2)
        self.assertEqual(plan_get.description, 'Description Plan 2')
        self.assertEqual(plan.duration, 2)
        self.assertEqual(plan.unit, 'Y')
        self.assertEqual(plan.recurring, False)

        plan_get.delete()
        self.assertEqual(plan_get._deleted, True)

        try:
            self.mc2p_client.Plan.get(plan.id)
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)

    def test_tax(self):
        tax_list = self.mc2p_client.tax.list()
        self.assertIsInstance(tax_list, base.Paginator)
        self.assertIsInstance(tax_list.results, list)
        self.assertIsInstance(tax_list.count, int)

        tax = self.mc2p_client.Tax({
            'name': 'Tax 1',
            'percent': 1
        })
        tax.save()
        self.assertEqual(tax.name, 'Tax 1')
        self.assertEqual(float(tax.percent), 1)

        tax.name = 'Tax 2'
        tax.percent = 2
        tax.save()
        self.assertEqual(tax.name, 'Tax 2')
        self.assertEqual(float(tax.percent), 2)

        tax_get = self.mc2p_client.Tax.get(tax.id)
        self.assertEqual(tax_get.id, tax.id)
        self.assertEqual(tax.name, 'Tax 2')
        self.assertEqual(float(tax.percent), 2)

        tax_get.delete()
        self.assertEqual(tax_get._deleted, True)

        try:
            self.mc2p_client.Tax.get(tax.id)
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)

    def test_shipping(self):
        shipping_list = self.mc2p_client.shipping.list()
        self.assertIsInstance(shipping_list, base.Paginator)
        self.assertIsInstance(shipping_list.results, list)
        self.assertIsInstance(shipping_list.count, int)

        shipping = self.mc2p_client.Shipping({
            'name': 'Shipping 1',
            'price': 1
        })
        shipping.save()
        self.assertEqual(shipping.name, 'Shipping 1')
        self.assertEqual(float(shipping.price), 1)

        shipping.name = 'Shipping 2'
        shipping.price = 2
        shipping.save()
        self.assertEqual(shipping.name, 'Shipping 2')
        self.assertEqual(float(shipping.price), 2)

        shipping_get = self.mc2p_client.Shipping.get(shipping.id)
        self.assertEqual(shipping_get.id, shipping.id)
        self.assertEqual(shipping.name, 'Shipping 2')
        self.assertEqual(float(shipping.price), 2)

        shipping_get.delete()
        self.assertEqual(shipping_get._deleted, True)

        try:
            self.mc2p_client.Shipping.get(shipping.id)
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)

    def test_coupon(self):
        coupon_list = self.mc2p_client.shipping.list()
        self.assertIsInstance(coupon_list, base.Paginator)
        self.assertIsInstance(coupon_list.results, list)
        self.assertIsInstance(coupon_list.count, int)

        coupon = self.mc2p_client.Coupon({
            'name': 'Coupon 1',
            'code': '123',
            'coupon_type': 'A',
            'value': 1,
            'total_uses': 1
        })
        coupon.save()
        self.assertEqual(coupon.name, 'Coupon 1')
        self.assertEqual(coupon.code, '123')
        self.assertEqual(coupon.coupon_type, 'A')
        self.assertEqual(float(coupon.value), 1)
        self.assertEqual(coupon.total_uses, 1)

        coupon.name = 'Coupon 2'
        coupon.code = 'ABC'
        coupon.coupon_type = 'P'
        coupon.value = 2
        coupon.total_uses = 2
        coupon.save()
        self.assertEqual(coupon.name, 'Coupon 2')
        self.assertEqual(coupon.code, 'ABC')
        self.assertEqual(coupon.coupon_type, 'P')
        self.assertEqual(float(coupon.value), 2)
        self.assertEqual(coupon.total_uses, 2)

        coupon_get = self.mc2p_client.Coupon.get(coupon.id)
        self.assertEqual(coupon_get.id, coupon.id)
        self.assertEqual(coupon.name, 'Coupon 2')
        self.assertEqual(coupon.code, 'ABC')
        self.assertEqual(coupon.coupon_type, 'P')
        self.assertEqual(float(coupon.value), 2)
        self.assertEqual(coupon.total_uses, 2)

        coupon_get.delete()
        self.assertEqual(coupon_get._deleted, True)

        try:
            self.mc2p_client.Coupon.get(coupon.id)
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)
