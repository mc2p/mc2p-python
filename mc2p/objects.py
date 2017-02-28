from .base import RetrieveObjectItem, DeleteSaveRetrieveObjectItem, CreateRetrieveObjectItem


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


class Transaction(CreateRetrieveObjectItem):
    """
    Transaction object
    """
    pass


class Subscription(CreateRetrieveObjectItem):
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
