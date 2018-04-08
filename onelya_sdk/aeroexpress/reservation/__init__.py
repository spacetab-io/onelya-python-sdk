from onelya_sdk.utils import get_datetime, get_array, get_item
from onelya_sdk.wrapper.types import ProviderPaymentForm
from .requests import (OrderFullCustomerRequest, OrderCustomerDocuments, AeroexpressReservationRequest,
                       AeroexpressAutoReturnRequest)
from onelya_sdk.wrapper import (OrderCreateReservationCustomerResponse, OrderCustomerResponse, ReservationResponse,
                                AeroexpressConfirmResponse, AeroexpressAutoReturnResponse)

CREATE_METHOD = 'Order/V1/Reservation/Create'
CONFIRM_METHOD = 'Order/V1/Reservation/Confirm'
BLANK_METHOD = 'Order/V1/Reservation/Blank'
CANCEL_METHOD = 'Order/V1/Reservation/Cancel'
VOID_METHOD = 'Order/V1/Reservation/Void'
AUTO_RETURN_METHOD = 'Order/V1/Reservation/AutoReturn'


class Reservation(object):

    def __init__(self, request_wrapper):
        self.request_wrapper = request_wrapper

    def create(self, customers: OrderFullCustomerRequest, reservation_items: AeroexpressReservationRequest,
               contact_phone=None, contact_emails=None):
        response = self.request_wrapper.make_request(CREATE_METHOD, customers=customers, contact_phone=contact_phone,
                                                     reservation_items=reservation_items, contact_emails=contact_emails)
        return CreateReservation(response)

    def confirm(self, order_id: int, provider_payment_form: ProviderPaymentForm,
                order_customer_ids: 'list of int'=None,
                order_customer_documents: 'list of OrderCustomerDocuments'=None):
        response = self.request_wrapper.make_request(CONFIRM_METHOD, order_id=order_id, order_customer_ids=order_customer_ids,
                                                     order_customer_documents=order_customer_documents,
                                                     provider_payment_form=provider_payment_form)
        return Confirm(response)

    def blank(self, order_id: int, order_item_id: int=None, retrieve_main_services: bool=True, retrieve_upsales: bool=True):

        response = self.request_wrapper.make_request(BLANK_METHOD, order_id=order_id, order_item_id=order_item_id,
                                                     retrieve_main_services=retrieve_main_services,
                                                     retrieve_upsales=retrieve_upsales)
        return Blank(response)

    def cancel(self, order_id: int, order_item_ids: 'list of int'=None, order_customer_ids: 'list of int'=None):
        self.request_wrapper.make_request(CANCEL_METHOD, order_id=order_id, order_item_ids=order_item_ids,
                                          order_customer_ids=order_customer_ids)
        return True

    def void(self, order_id: int, order_item_ids: 'list of int'=None, order_customer_ids: 'list of int'=None):
        response = self.request_wrapper.make_request(VOID_METHOD, order_id=order_id, order_item_ids=order_item_ids,
                                                     order_customer_ids=order_customer_ids)
        return Void(response)

    def auto_return(self, order_item_id: int, agent_reference_id: str=None):
        response = self.request_wrapper.make_request(AUTO_RETURN_METHOD,
                                                     service_auto_return_request=AeroexpressAutoReturnRequest(
                                                         order_item_id, agent_reference_id))
        return AutoReturn(response)


class CreateReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId')
        self.amount = json_data.get('Amount')
        self.confirm_till = get_datetime(json_data.get('ConfirmTill'))
        self.customers = get_array(json_data.get('Customers'), OrderCreateReservationCustomerResponse)
        self.reservation_results = get_array(json_data.get('ReservationResults'), ReservationResponse)

        self.json_data = json_data


class ProlongReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId')
        self.confirm_till = get_datetime(json_data.get('ConfirmTill'))

        self.json_data = json_data


class Confirm(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId')
        self.customers = get_array(json_data.get('Customers'),  OrderCustomerResponse)
        self.confirm_results = get_array(json_data.get('ConfirmResults'), AeroexpressConfirmResponse)

        self.json_data = json_data


class Blank(object):
    def __init__(self, data):
        self.__data = data

    def save_blank(self, path):
        open(path, 'wb').write(self.content)

    @property
    def content(self):
        return self.__data.content


class Void(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId')

        self.json_data = json_data


class AutoReturn(object):
    def __init__(self, json_data):
        self.service_return_response = get_item(json_data.get('ServiceReturnResponse'), AeroexpressAutoReturnResponse)

        self.json_data = json_data
