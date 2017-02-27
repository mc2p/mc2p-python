from .request import APIRequest
from .resources import ProductResource, PlanResource, TaxResource, ShippingResource, CouponResource, \
    TransactionResource, SubscriptionResource, SaleResource, CurrencyResource, GatewayResource


class MC2P(object):
    def __init__(self, key, secret_key):
        self.api_request = APIRequest(key, secret_key)

        self.product = ProductResource(self.api_request)
        self.plan = PlanResource(self.api_request)
        self.tax = TaxResource(self.api_request)
        self.shipping = ShippingResource(self.api_request)
        self.coupon = CouponResource(self.api_request)
        self.transaction = TransactionResource(self.api_request)
        self.subscription = SubscriptionResource(self.api_request)
        self.sale = SaleResource(self.api_request)
        self.currency = CurrencyResource(self.api_request)
        self.gateway = GatewayResource(self.api_request)
