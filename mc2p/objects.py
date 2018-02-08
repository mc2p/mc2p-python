from .base import ReadOnlyObjectItem, CRUDObjectItem, CRObjectItem
from .mixin import PayURLMixin, RefundCaptureVoidObjectItemMixin, CardShareObjectItemMixin, ChargeObjectItemMixin


class Product(CRUDObjectItem):
    """
    Product object
    """
    pass


class Plan(CRUDObjectItem):
    """
    Plan object
    """
    pass


class Tax(CRUDObjectItem):
    """
    Tax object
    """
    pass


class Shipping(CRUDObjectItem):
    """
    Shipping object
    """
    pass


class Coupon(CRUDObjectItem):
    """
    Coupon object
    """
    pass


class Transaction(PayURLMixin, CRObjectItem):
    """
    Transaction object
    """
    pass


class Subscription(PayURLMixin, CRObjectItem):
    """
    Subscription object
    """
    pass


class Authorization(ChargeObjectItemMixin, PayURLMixin, CRObjectItem):
    """
    Authorization object
    """
    pass


class Sale(RefundCaptureVoidObjectItemMixin, ReadOnlyObjectItem):
    """
    Sale object
    """
    pass


class Currency(ReadOnlyObjectItem):
    """
    Currency object
    """
    pass


class Gateway(ReadOnlyObjectItem):
    """
    Gateway object
    """
    pass


class PayData(CardShareObjectItemMixin, ReadOnlyObjectItem):
    """
    PayData object
    """
    ID_PROPERTY = 'token'

