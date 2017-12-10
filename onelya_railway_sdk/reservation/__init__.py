from ..utils import get_datetime, get_array
from ..wrapper.requests import RequestWrapper
from ..wrapper.types import ProlongReservationType, ProviderPaymentForm
from .requests import OrderFullCustomerRequest, RailwayReservationRequest, OrderCustomerDocuments
from ..wrapper import OrderCreateReservationCustomerResponse, RailwayReservationResponse, OrderCustomerResponse, RailwayConfirmResponse

CREATE_METHOD = 'Order/V1/Reservation/Create'
PROLONG_RESERVATION_METHOD = 'Order/V1/Reservation/ProlongReservation'
CONFIRM_METHOD = 'Order/V1/Reservation/Confirm'
BLANK_METHOD = 'Order/V1/Reservation/Blank'


class Reservation(object):

    def __init__(self, session):
        self.session = session
        self.request_wrapper = RequestWrapper(self.session)

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
