from .base import Resource, ReadOnlyResource, CreateReadOnlyResource


class ProductResource(Resource):
    URL = '/product/'


class PlanResource(Resource):
    URL = '/plan/'


class TaxResource(Resource):
    URL = '/tax/'


class ShippingResource(Resource):
    URL = '/shipping/'


class CouponResource(Resource):
    URL = '/coupon/'


class TransactionResource(CreateReadOnlyResource):
    URL = '/transaction/'


class SubscriptionResource(CreateReadOnlyResource):
    URL = '/subscription/'


class SaleResource(ReadOnlyResource):
    URL = '/sale/'


class CurrencyResource(ReadOnlyResource):
    URL = '/currency/'


class GatewayResource(ReadOnlyResource):
    URL = '/gateway/'

