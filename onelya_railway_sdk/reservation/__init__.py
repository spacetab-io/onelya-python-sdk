from ..wrapper.requests import RequestWrapper
from .requests import ServiceReturnAmountRequest
from ..utils import get_datetime, get_array, get_item
from ..wrapper.types import ProlongReservationType, ProviderPaymentForm
from .requests import (OrderFullCustomerRequest, RailwayReservationRequest, OrderCustomerDocuments,
                       ServiceAutoReturnRequest, ServiceAddUpsaleRequest)
from ..wrapper import (OrderCreateReservationCustomerResponse, RailwayReservationResponse, OrderCustomerResponse,
                       RailwayConfirmResponse, RailwayReturnAmountResponse, RailwayAutoReturnResponse,
                       CustomerUpsaleOperationResult)

CREATE_METHOD = 'Order/V1/Reservation/Create'
PROLONG_RESERVATION_METHOD = 'Order/V1/Reservation/ProlongReservation'
CONFIRM_METHOD = 'Order/V1/Reservation/Confirm'
BLANK_METHOD = 'Order/V1/Reservation/Blank'
CANCEL_METHOD = 'Order/V1/Reservation/Cancel'
RETURN_AMOUNT_METHOD = 'Order/V1/Reservation/ReturnAmount'
AUTO_RETURN_METHOD = 'Order/V1/Reservation/AutoReturn'
ADD_UPSALE_METHOD = 'Order/V1/Reservation/AddUpsale'
REFUSE_UPSALE_METHOD = 'Order/V1/Reservation/RefuseUpsale'


class Reservation(object):

    def __init__(self, session):
        self.request_wrapper = RequestWrapper(session)

    def create(self, customers: OrderFullCustomerRequest, reservation_items: RailwayReservationRequest,
               contact_phone=None, contact_emails=None):
        response = self.request_wrapper.make_request(CREATE_METHOD, customers=customers, contact_phone=contact_phone,
                                                     reservation_items=reservation_items, contact_emails=contact_emails)
        return CreateReservation(response)

    def prolong_reservation(self, order_id: int, order_item_ids: 'list of int'=None,
                            prolong_reservation_type: ProlongReservationType=ProlongReservationType.RAILWAY_THREE_HOURS_RESERVATION):
        response = self.request_wrapper.make_request(PROLONG_RESERVATION_METHOD, order_id=order_id,
                                                     prolong_reservation_type=prolong_reservation_type,
                                                     order_item_ids=order_item_ids)
        return ProlongReservation(response)

    def confirm(self, order_id: int, order_customer_ids: 'list of int'=None,
                order_customer_documents: 'lisf of OrderCustomerDocuments'=None,
                provider_payment_form: ProviderPaymentForm=None):
        response = self.request_wrapper.make_request(CONFIRM_METHOD, order_id=order_id, order_customer_ids=order_customer_ids,
                                                     order_customer_documents=order_customer_documents,
                                                     provider_payment_form=provider_payment_form)
        return Confirm(response)

    def blank(self, order_id: int, order_item_id: int, retrieve_main_services: bool=True, retrieve_upsales: bool=True):

        response = self.request_wrapper.make_request(BLANK_METHOD, order_id=order_id, order_item_id=order_item_id,
                                                     retrieve_main_services=retrieve_main_services,
                                                     retrieve_upsales=retrieve_upsales)
        return Blank(response)

    def cancel(self, order_id: int, order_item_ids: 'list of int'=None, order_customer_ids: 'list of int'=None):
        self.request_wrapper.make_request(CANCEL_METHOD, order_id=order_id, order_item_ids=order_item_ids,
                                          order_customer_ids=order_customer_ids)
        return True

    def return_amount(self, check_document_number: str, order_item_id: int, order_item_blank_ids: 'list of int'=None):
        response = self.request_wrapper.make_request(RETURN_AMOUNT_METHOD,
                                                     service_return_amount_request=ServiceReturnAmountRequest(
                                                         check_document_number, order_item_id, order_item_blank_ids))
        return ReturnAmount(response)

    def auto_return(self, check_document_number: str, order_item_id: int, order_item_blank_ids: 'list of int'=None,
                    agent_reference_id: str=None):
        response = self.request_wrapper.make_request(AUTO_RETURN_METHOD,
                                                     service_auto_return_request=ServiceAutoReturnRequest(
                                                         check_document_number, order_item_id, order_item_blank_ids,
                                                         agent_reference_id))
        return AutoReturn(response)

    def add_upsale(self, order_id: int, order_item_id: int=None, service_add_upsale_request: ServiceAddUpsaleRequest=None):
        response = self.request_wrapper.make_request(ADD_UPSALE_METHOD, order_id=order_id, order_item_id=order_item_id,
                                                     service_add_upsale_request=service_add_upsale_request)
        return AddUpsale(response)

    def refuse_upsale(self, order_id: int=None, order_item_id: int=None, order_customer_ids: 'list of int'=None):
        response = self.request_wrapper.make_request(REFUSE_UPSALE_METHOD, order_id=order_id, order_item_id=order_item_id,
                                                     order_customer_ids=order_customer_ids)
        return RefuseUpsale(response)


class CreateReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.amount = json_data.get('Amount', None)
        self.confirm_till = get_datetime(json_data.get('ConfirmTill', None))
        self.customers = get_array(json_data.get('Customers', None), OrderCreateReservationCustomerResponse)
        self.reservation_results = get_array(json_data.get('ReservationResults', None), RailwayReservationResponse)

        self.json_data = json_data


class ProlongReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.confirm_till = get_datetime(json_data.get('ConfirmTill', None))

        self.json_data = json_data


class Confirm(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.customers = get_array(json_data.get('Customers', None),  OrderCustomerResponse)
        self.confirm_results = get_array(json_data.get('ConfirmResults', None), RailwayConfirmResponse)

        self.json_data = json_data


class Blank(object):
    def __init__(self, data):
        self.__data = data

    def save_blank(self, path):
        open(path, 'wb').write(self.content)

    @property
    def content(self):
        return self.__data.content


class ReturnAmount(object):
    def __init__(self, json_data):
        self.service_return_response = get_item(json_data.get('ServiceReturnResponse', None), RailwayReturnAmountResponse)

        self.json_data = json_data


class AutoReturn(object):
    def __init__(self, json_data):
        self.service_return_response = get_item(json_data.get('ServiceReturnResponse', None), RailwayAutoReturnResponse)

        self.json_data = json_data


class AddUpsale(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.upsale_results = get_array(json_data.get('UpsaleResults', None), CustomerUpsaleOperationResult)

        self.json_data = json_data


class RefuseUpsale(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)

        self.json_data = json_data
