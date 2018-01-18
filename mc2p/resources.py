from .mixin import RefundCaptureVoidResourceMixin, CardShareResourceMixin, ChargeResourceMixin
from .base import DetailOnlyResource, ReadOnlyResource, CRResource, CRUDResource
from .objects import Product, Plan, Tax, Shipping, Coupon, Transaction, Subscription, Authorization, Sale, Currency, \
    Gateway, PayData


class ProductResource(CRUDResource):
    """
    Product resource
    """
    PATH = '/product/'
    OBJECT_ITEM_CLASS = Product


class PlanResource(CRUDResource):
    """
    Plan resource
    """
    PATH = '/plan/'
    OBJECT_ITEM_CLASS = Plan


class TaxResource(CRUDResource):
    """
    Tax resource
    """
    PATH = '/tax/'
    OBJECT_ITEM_CLASS = Tax


class ShippingResource(CRUDResource):
    """
    Shipping resource
    """
    PATH = '/shipping/'
    OBJECT_ITEM_CLASS = Shipping


class CouponResource(CRUDResource):
    """
    Coupon resource
    """
    PATH = '/coupon/'
    OBJECT_ITEM_CLASS = Coupon


class TransactionResource(CRResource):
    """
    Transaction resource
    """
    PATH = '/transaction/'
    OBJECT_ITEM_CLASS = Transaction


class SubscriptionResource(CRResource):
    """
    Subscription resource
    """
    PATH = '/subscription/'
    OBJECT_ITEM_CLASS = Subscription


class AuthorizationResource(ChargeResourceMixin, CRResource):
    """
    Authorization resource
    """
    PATH = '/authorization/'
    OBJECT_ITEM_CLASS = Authorization


class SaleResource(RefundCaptureVoidResourceMixin, ReadOnlyResource):
    """
    Sale resource
    """
    PATH = '/sale/'
    OBJECT_ITEM_CLASS = Sale


class CurrencyResource(ReadOnlyResource):
    """
    Currency resource
    """
    PATH = '/currency/'
    OBJECT_ITEM_CLASS = Currency


class GatewayResource(ReadOnlyResource):
    """
    Gateway resource
    """
    PATH = '/gateway/'
    OBJECT_ITEM_CLASS = Gateway


class PayDataResource(CardShareResourceMixin, DetailOnlyResource):
    """
    PayData resource
    """
    PATH = '/pay/'
    OBJECT_ITEM_CLASS = PayData

