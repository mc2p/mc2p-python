from .base import ObjectItem, ReadOnlyObjectItem, CreateReadOnlyObjectItem


class Product(ObjectItem):
    pass


class Plan(ObjectItem):
    pass


class Tax(ObjectItem):
    pass


class Shipping(ObjectItem):
    pass


class Coupon(ObjectItem):
    pass


class Transaction(CreateReadOnlyObjectItem):
    pass


class Subscription(CreateReadOnlyObjectItem):
    pass


class Sale(ReadOnlyObjectItem):
    pass


class Currency(ReadOnlyObjectItem):
    pass


class Gateway(ReadOnlyObjectItem):
    pass
