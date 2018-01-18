class NotificationData(object):
    """
    Notification data - class to manage notification from MyChoice2Pay
    """
    def __init__(self, json_body, mc2p):
        """
        Initializes a notification data
        :param json_body: content of request from MyChoice2Pay
        :param mc2p: MC2PClient
        """
        self.json_body = json_body
        self.mc2p = mc2p

    @property
    def status(self):
        """
        :return: status of payment
        """
        return self.json_body['status']

    @property
    def subscription_status(self):
        """
        :return: status of subscription
        """
        return self.json_body['subscription_status']

    @property
    def authorization_status(self):
        """
        :return: status of authorization
        """
        return self.json_body['authorization_status']

    @property
    def type(self):
        """
        :return: type of payment
        """
        return self.json_body['type']

    @property
    def order_id(self):
        """
        :return: order_id sent when payment was created
        """
        return self.json_body['order_id']

    @property
    def action(self):
        """
        :return: action executed
        """
        return self.json_body['action']

    @property
    def transaction(self):
        """
        :return: transaction generated when payment was created
        """
        if self.type != 'P':
            return None

        return self.mc2p.Transaction.get(self.json_body['id'])

    @property
    def subscription(self):
        """
        :return: subscription generated when payment was created
        """
        if self.type != 'S':
            return None

        return self.mc2p.Subscription.get(self.json_body['id'])

    @property
    def sale(self):
        """
        :return: sale generated when payment was paid
        """
        if not self.json_body.get('sale_id', False):
            return None

        return self.mc2p.Sale.get(self.json_body['sale_id'])

    @property
    def sale_action(self):
        """
        :return: action of sale executed
        """
        return self.json_body['sale_action']
