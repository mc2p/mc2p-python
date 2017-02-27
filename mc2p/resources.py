from .base import Resource, ReadOnlyResource, CreateReadOnlyResource
from .objects import Product, Plan, Tax, Shipping, Coupon, Transaction, Subscription, Sale, Currency, Gateway


class ProductResource(Resource):
    URL = '/product/'
    OBJECT_ITEM_CLASS = Product


class PlanResource(Resource):
    URL = '/plan/'
    OBJECT_ITEM_CLASS = Plan


class TaxResource(Resource):
    URL = '/tax/'
    OBJECT_ITEM_CLASS = Tax


class ShippingResource(Resource):
    URL = '/shipping/'
    OBJECT_ITEM_CLASS = Shipping


class CouponResource(Resource):
    URL = '/coupon/'
    OBJECT_ITEM_CLASS = Coupon


class TransactionResource(CreateReadOnlyResource):
    URL = '/transaction/'
    OBJECT_ITEM_CLASS = Transaction


class SubscriptionResource(CreateReadOnlyResource):
    URL = '/subscription/'
    OBJECT_ITEM_CLASS = Subscription


class SaleResource(ReadOnlyResource):
    URL = '/sale/'
    OBJECT_ITEM_CLASS = Sale


class CurrencyResource(ReadOnlyResource):
    URL = '/currency/'
    OBJECT_ITEM_CLASS = Currency


class GatewayResource(ReadOnlyResource):
    URL = '/gateway/'
    OBJECT_ITEM_CLASS = Gateway

