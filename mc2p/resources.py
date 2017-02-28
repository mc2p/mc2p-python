from .base import ListDetailResource, CreateListDetailResource, DeleteChangeCreateListDetailResource
from .objects import Product, Plan, Tax, Shipping, Coupon, Transaction, Subscription, Sale, Currency, Gateway


class ProductResource(DeleteChangeCreateListDetailResource):
    """
    Product resource
    """
    URL = '/product/'
    OBJECT_ITEM_CLASS = Product


class PlanResource(DeleteChangeCreateListDetailResource):
    """
    Plan resource
    """
    URL = '/plan/'
    OBJECT_ITEM_CLASS = Plan


class TaxResource(DeleteChangeCreateListDetailResource):
    """
    Tax resource
    """
    URL = '/tax/'
    OBJECT_ITEM_CLASS = Tax


class ShippingResource(DeleteChangeCreateListDetailResource):
    """
    Shipping resource
    """
    URL = '/shipping/'
    OBJECT_ITEM_CLASS = Shipping


class CouponResource(DeleteChangeCreateListDetailResource):
    """
    Coupon resource
    """
    URL = '/coupon/'
    OBJECT_ITEM_CLASS = Coupon


class TransactionResource(CreateListDetailResource):
    """
    Transaction resource
    """
    URL = '/transaction/'
    OBJECT_ITEM_CLASS = Transaction


class SubscriptionResource(CreateListDetailResource):
    """
    Subscription resource
    """
    URL = '/subscription/'
    OBJECT_ITEM_CLASS = Subscription


class SaleResource(ListDetailResource):
    """
    Sale resource
    """
    URL = '/sale/'
    OBJECT_ITEM_CLASS = Sale


class CurrencyResource(ListDetailResource):
    """
    Currency resource
    """
    URL = '/currency/'
    OBJECT_ITEM_CLASS = Currency


class GatewayResource(ListDetailResource):
    """
    Gateway resource
    """
    URL = '/gateway/'
    OBJECT_ITEM_CLASS = Gateway

