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

    def test_transaction(self):
        transaction_list = self.mc2p_client.transaction.list()
        self.assertIsInstance(transaction_list, base.Paginator)
        self.assertIsInstance(transaction_list.results, list)
        self.assertIsInstance(transaction_list.count, int)
        next_transaction_list = transaction_list.get_next_list()
        self.assertIsInstance(next_transaction_list, base.Paginator)
        self.assertIsInstance(next_transaction_list.results, list)
        self.assertIsInstance(next_transaction_list.count, int)
        previous_transaction_list = next_transaction_list.get_previous_list()
        self.assertIsInstance(previous_transaction_list, base.Paginator)
        self.assertIsInstance(previous_transaction_list.results, list)
        self.assertIsInstance(previous_transaction_list.count, int)

        transaction = self.mc2p_client.Transaction({
            'currency': 'EUR',
            'products': [{
                'amount': 1,
                'product': {
                    'name': 'Product',
                    'price': 5
                }
            }]
        })
        transaction.save()
        self.assertEqual(transaction.currency, 'EUR')
        self.assertIsInstance(transaction.products, list)
        self.assertIsInstance(transaction.pay_url, str)
        self.assertIsInstance(transaction.iframe_url, str)
        self.assertEqual(transaction.products[0]['amount'], 1)
        self.assertEqual(transaction.products[0]['product']['name'], 'Product')
        self.assertEqual(float(transaction.products[0]['product']['price']), 5)

        transaction_get = self.mc2p_client.Transaction.get(transaction.id)
        self.assertEqual(transaction_get.id, transaction.id)
        self.assertEqual(transaction_get.currency, 'EUR')
        self.assertIsInstance(transaction_get.products, list)
        self.assertIsInstance(transaction_get.pay_url, str)
        self.assertIsInstance(transaction_get.iframe_url, str)
        self.assertEqual(transaction_get.products[0]['amount'], 1)
        self.assertEqual(transaction_get.products[0]['product']['name'], 'Product')
        self.assertEqual(float(transaction_get.products[0]['product']['price']), 5)

    def test_subscription(self):
        subscription_list = self.mc2p_client.subscription.list()
        self.assertIsInstance(subscription_list, base.Paginator)
        self.assertIsInstance(subscription_list.results, list)
        self.assertIsInstance(subscription_list.count, int)

        subscription = self.mc2p_client.Subscription({
            'currency': 'EUR',
            'plan': {
                'name': 'Plan',
                'price': 5,
                'duration': 1,
                'unit': 'M',
                'recurring': True
            },
            'note': 'Note example'
        })
        subscription.save()
        self.assertEqual(subscription.currency, 'EUR')
        self.assertIsInstance(subscription.pay_url, str)
        self.assertIsInstance(subscription.iframe_url, str)
        self.assertEqual(subscription.plan['name'], 'Plan')
        self.assertEqual(float(subscription.plan['price']), 5)
        self.assertEqual(subscription.plan['duration'], 1)
        self.assertEqual(subscription.plan['unit'], 'M')
        self.assertEqual(subscription.plan['recurring'], True)

        subscription_get = self.mc2p_client.Subscription.get(subscription.id)
        self.assertEqual(subscription_get.id, subscription.id)
        self.assertEqual(subscription_get.currency, 'EUR')
        self.assertIsInstance(subscription_get.pay_url, str)
        self.assertIsInstance(subscription_get.iframe_url, str)
        self.assertEqual(subscription_get.plan['name'], 'Plan')
        self.assertEqual(float(subscription_get.plan['price']), 5)
        self.assertEqual(subscription_get.plan['duration'], 1)
        self.assertEqual(subscription_get.plan['unit'], 'M')
        self.assertEqual(subscription_get.plan['recurring'], True)

    def test_sale(self):
        sale_list = self.mc2p_client.sale.list()
        self.assertIsInstance(sale_list, base.Paginator)
        self.assertIsInstance(sale_list.results, list)
        self.assertIsInstance(sale_list.count, int)

        sale = self.mc2p_client.Sale.get('d1bb7082-7a97-48c6-893d-4d5febcd463b')
        self.assertEqual(sale.id, 'd1bb7082-7a97-48c6-893d-4d5febcd463b')
        self.assertEqual(float(sale.amount), 5)

        result = sale.refund()
        self.assertEqual(result['success'], False)

        result = sale.capture()
        self.assertEqual(result['success'], False)

        result = sale.void()
        self.assertEqual(result['success'], False)

    def test_currency(self):
        currency_list = self.mc2p_client.currency.list()
        self.assertIsInstance(currency_list, base.Paginator)
        self.assertIsInstance(currency_list.results, list)
        self.assertIsInstance(currency_list.count, int)

        currency = self.mc2p_client.Currency.get('5d978f20-21c2-4315-98de-d1c117113e7b')
        self.assertEqual(currency.id, '5d978f20-21c2-4315-98de-d1c117113e7b')
        self.assertEqual(currency.name, 'Euro')
        self.assertEqual(currency.code, 'EUR')

    def test_gateway(self):
        gateway_list = self.mc2p_client.gateway.list()
        self.assertIsInstance(gateway_list, base.Paginator)
        self.assertIsInstance(gateway_list.results, list)
        self.assertIsInstance(gateway_list.count, int)

    def test_pay_data(self):
        pay_data = self.mc2p_client.PayData.get('c11e3d0b374945609ea451183665f581')
        self.assertEqual(pay_data.app_name, 'GitHub Test')
        self.assertEqual(pay_data.transaction['token'], 'c11e3d0b374945609ea451183665f581')
        self.assertIsInstance(pay_data.gateways, list)
        self.assertEqual(pay_data.gateways[0]['name'], 'Divvy')
        self.assertEqual(pay_data.gateways[0]['code'], 'DVG')
        self.assertEqual(pay_data.gateways[0]['form'], 'shared')

        try:
             pay_data.card('DVG', {})
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)
            self.assertIsInstance(e.json_body, dict)

        try:
             pay_data.share({})
        except Exception as e:
            self.assertIsInstance(e, errors.MC2PError)
            self.assertIsInstance(e.json_body, dict)

    def test_notification_data(self):
        # JSON data received in the notification url
        notification_data = self.mc2p_client.NotificationData({
            'status': 'D',
            'subscription_status': '',
            'type': 'P',
            'order_id': '',
            'action': 'D',
            'id': 'c8325bb3-c24e-4c0c-b0ff-14fe89bf9f1f',
            'sale_id': 'd1bb7082-7a97-48c6-893d-4d5febcd463b',
            'sale_action': 'G'

        })
        self.assertEqual(notification_data.status, 'D')
        self.assertEqual(notification_data.subscription_status, '')
        self.assertEqual(notification_data.type, 'P')
        self.assertEqual(notification_data.order_id, '')
        self.assertEqual(notification_data.action, 'D')
        self.assertEqual(notification_data.sale_action, 'G')
        self.assertIsInstance(notification_data.transaction, objects.Transaction)
        self.assertEqual(notification_data.transaction.id, 'c8325bb3-c24e-4c0c-b0ff-14fe89bf9f1f')
        self.assertIsInstance(notification_data.sale, objects.Sale)
        self.assertEqual(notification_data.sale.id, 'd1bb7082-7a97-48c6-893d-4d5febcd463b')
