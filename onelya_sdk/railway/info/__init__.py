from datetime import datetime
from onelya_sdk.utils import get_array, get_datetime, get_item
from onelya_sdk.wrapper.types import OperationType, ProviderPaymentForm
from onelya_sdk.wrapper import OrderCustomerInfo, RailwayFullOrderItemInfo, RailwayShortOrderInfo

ORDER_INFO_METHOD = 'Order/V1/Info/OrderInfo'
ORDER_LIST_METHOD = 'Order/V1/Info/OrderList'


class Info(object):
    def __init__(self, request_wrapper):
        self.__request_wrapper = request_wrapper

    def info(self, order_id: int=None, agent_reference_id: str=None):
        response = self.__request_wrapper.make_request(ORDER_INFO_METHOD, order_id=order_id,
                                                       agent_reference_id=agent_reference_id)
        return OrderInfo(response)

    def list(self, date: datetime=None, operation_type: OperationType=None,
             provider_payment_form: ProviderPaymentForm=None, is_externally_loaded: bool=None):
        response = self.__request_wrapper.make_request(ORDER_LIST_METHOD, date=date, operation_type=operation_type,
                                                       provider_payment_form=provider_payment_form,
                                                       is_externally_loaded=is_externally_loaded)
        return OrderList(response)


class OrderInfo(object):
    def __init__(self, json_data):
        self.order_customers = get_array(json_data.get('OrderCustomers'), OrderCustomerInfo)
        self.order_items = get_array(json_data.get('OrderItems'), RailwayFullOrderItemInfo)
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.contact_phone = json_data.get('ContactPhone')
        self.contact_emails = json_data.get('ContactEmails')
        self.created = get_datetime(json_data.get('Created'))
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.pos_sys_name = json_data.get('PosSysName')

        self.json_data = json_data


class OrderList(object):
    def __init__(self, json_data):
        self.orders = get_array(json_data.get('Orders'), RailwayShortOrderInfo)

        self.json_data = json_data
