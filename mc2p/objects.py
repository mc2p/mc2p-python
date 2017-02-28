from .base import RetrieveObjectItem, DeleteSaveRetrieveObjectItem, CreateRetrieveObjectItem
from .mixin import PayURLMixin


class Product(DeleteSaveRetrieveObjectItem):
    """
    Product object
    """
    pass


class Plan(DeleteSaveRetrieveObjectItem):
    """
    Plan object
    """
    pass


class Tax(DeleteSaveRetrieveObjectItem):
    """
    Tax object
    """
    pass


class Shipping(DeleteSaveRetrieveObjectItem):
    """
    Shipping object
    """
    pass


class Coupon(DeleteSaveRetrieveObjectItem):
    """
    Coupon object
    """
    pass


class Transaction(PayURLMixin, CreateRetrieveObjectItem):
    """
    Transaction object
    """
    pass


class Subscription(PayURLMixin, CreateRetrieveObjectItem):
    """
    Subscription object
    """
    pass


class Sale(RetrieveObjectItem):
    """
    Sale object
    """
    pass


class Currency(RetrieveObjectItem):
    """
    Currency object
    """
    pass


class Gateway(RetrieveObjectItem):
    """
    Gateway object
    """
    pass
