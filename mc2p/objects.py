from .base import RetrieveObjectItemMixin, DeleteSaveRetrieveObjectItem, CreateRetrieveObjectItem


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


class Sale(RetrieveObjectItemMixin):
    pass


class Currency(RetrieveObjectItemMixin):
    pass


class Gateway(RetrieveObjectItemMixin):
    pass
