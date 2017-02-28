from .base import ListDetailResource, CreateListDetailResource, DeleteChangeCreateListDetailResource
from .objects import Product, Plan, Tax, Shipping, Coupon, Transaction, Subscription, Sale, Currency, Gateway


class ProductResource(DeleteChangeCreateListDetailResource):
    URL = '/product/'
    OBJECT_ITEM_CLASS = Product


class PlanResource(DeleteChangeCreateListDetailResource):
    URL = '/plan/'
    OBJECT_ITEM_CLASS = Plan


class TaxResource(DeleteChangeCreateListDetailResource):
    URL = '/tax/'
    OBJECT_ITEM_CLASS = Tax


class ShippingResource(DeleteChangeCreateListDetailResource):
    URL = '/shipping/'
    OBJECT_ITEM_CLASS = Shipping


class CouponResource(DeleteChangeCreateListDetailResource):
    URL = '/coupon/'
    OBJECT_ITEM_CLASS = Coupon


class TransactionResource(CreateListDetailResource):
    URL = '/transaction/'
    OBJECT_ITEM_CLASS = Transaction


class SubscriptionResource(CreateListDetailResource):
    URL = '/subscription/'
    OBJECT_ITEM_CLASS = Subscription


class SaleResource(ListDetailResource):
    URL = '/sale/'
    OBJECT_ITEM_CLASS = Sale


class CurrencyResource(ListDetailResource):
    URL = '/currency/'
    OBJECT_ITEM_CLASS = Currency


class GatewayResource(ListDetailResource):
    URL = '/gateway/'
    OBJECT_ITEM_CLASS = Gateway

