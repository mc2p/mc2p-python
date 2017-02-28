from .base import RetrieveObjectItem, DeleteSaveRetrieveObjectItem, CreateRetrieveObjectItem


class Product(DeleteSaveRetrieveObjectItem):
    pass


class Plan(DeleteSaveRetrieveObjectItem):
    pass


class Tax(DeleteSaveRetrieveObjectItem):
    pass


class Shipping(DeleteSaveRetrieveObjectItem):
    pass


class Coupon(DeleteSaveRetrieveObjectItem):
    pass


class Transaction(CreateRetrieveObjectItem):
    pass


class Subscription(CreateRetrieveObjectItem):
    pass


class Sale(RetrieveObjectItem):
    pass


class Currency(RetrieveObjectItem):
    pass


class Gateway(RetrieveObjectItem):
    pass
