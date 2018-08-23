from .requests import ServiceReturnAmountRequest
from onelya_sdk.utils import get_datetime, get_array, get_item, get_bool_item
from onelya_sdk.wrapper.types import ProlongReservationType, ProviderPaymentForm, ReturnTarget
from .requests import (OrderFullCustomerRequest, RailwayReservationRequest, OrderCustomerDocuments,
                       ServiceAutoReturnRequest, ServiceAddUpsaleRequest)
from onelya_sdk.wrapper import (OrderCreateReservationCustomerResponse, ReservationResponse, OrderCustomerResponse,
                                RailwayConfirmResponse, RailwayReturnAmountResponse, RailwayAutoReturnResponse,
                                CustomerUpsaleOperationResult, RailwayBlankInfo)

CREATE_METHOD = 'Order/V1/Reservation/Create'
PROLONG_RESERVATION_METHOD = 'Order/V1/Reservation/ProlongReservation'
CONFIRM_METHOD = 'Order/V1/Reservation/Confirm'
BLANK_METHOD = 'Order/V1/Reservation/Blank'
CANCEL_METHOD = 'Order/V1/Reservation/Cancel'
RETURN_AMOUNT_METHOD = 'Order/V1/Reservation/ReturnAmount'
AUTO_RETURN_METHOD = 'Order/V1/Reservation/AutoReturn'
ADD_UPSALE_METHOD = 'Order/V1/Reservation/AddUpsale'
REFUSE_UPSALE_METHOD = 'Order/V1/Reservation/RefuseUpsale'

UPDATE_BLANKS_METHOD = 'Railway/V1/Reservation/UpdateBlanks'
ELECTRONIC_REGISTRATION_METHOD = 'Railway/V1/Reservation/ElectronicRegistration'
MEAL_OPTION_METHOD = 'Railway/V1/Reservation/MealOption'
BLANK_AS_HTML_METHOD = 'Railway/V1/Reservation/BlankAsHtml'


class Reservation(object):

    def __init__(self, request_wrapper):
        self.request_wrapper = request_wrapper

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

    def confirm(self, order_id: int, provider_payment_form: ProviderPaymentForm,
                order_customer_ids: 'list of int'=None,
                order_customer_documents: 'lisf of OrderCustomerDocuments'=None):
        response = self.request_wrapper.make_request(CONFIRM_METHOD, order_id=order_id, order_customer_ids=order_customer_ids,
                                                     order_customer_documents=order_customer_documents,
                                                     provider_payment_form=provider_payment_form)
        return Confirm(response)

    def blank(self, order_id: int, order_item_id: int, order_item_ids: 'list of int', retrieve_main_services: bool=True,
              retrieve_upsales: bool=True):

        response = self.request_wrapper.make_request(BLANK_METHOD, order_id=order_id, order_item_id=order_item_id,
                                                     order_item_ids=order_item_ids,
                                                     retrieve_main_services=retrieve_main_services,
                                                     retrieve_upsales=retrieve_upsales)
        return Blank(response)

    def cancel(self, order_id: int, order_item_ids: 'list of int'=None, order_customer_ids: 'list of int'=None):
        self.request_wrapper.make_request(CANCEL_METHOD, order_id=order_id, order_item_ids=order_item_ids,
                                          order_customer_ids=order_customer_ids)
        return True

    def return_amount(self, check_document_number: str, order_item_id: int, order_item_blank_ids: 'list of int'=None,
                      return_target: ReturnTarget=None):
        response = self.request_wrapper.make_request(RETURN_AMOUNT_METHOD,
                                                     service_return_amount_request=ServiceReturnAmountRequest(
                                                         check_document_number, order_item_id, order_item_blank_ids,
                                                         return_target))
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

    def update_blanks(self, order_item_id: int):
        response = self.request_wrapper.make_request(UPDATE_BLANKS_METHOD, order_item_id=order_item_id)
        return UpdateBlanks(response)

    def electronic_registration(self, order_item_id: int, set: bool, order_item_blank_ids: 'list of int'=None,
                                send_notification: bool=False):
        response = self.request_wrapper.make_request(ELECTRONIC_REGISTRATION_METHOD, order_item_id=order_item_id,
                                                     set=set, order_item_blank_ids=order_item_blank_ids,
                                                     send_notification=send_notification)
        return ElectronicRegistration(response)

    def meal_option(self, order_item_id: int, meal_option_code: str, order_item_blank_id: int):
        response = self.request_wrapper.make_request(MEAL_OPTION_METHOD, order_item_id=order_item_id,
                                                     meal_option_code=meal_option_code,
                                                     order_item_blank_id=order_item_blank_id)
        return MealOption(response)

    def blank_as_html(self, order_item_id: int, order_item_ids: 'list of int'=None):
        response = self.request_wrapper.make_request(BLANK_AS_HTML_METHOD, order_item_id=order_item_id,
                                                     order_item_ids=order_item_ids)
        return BlankAsHtml(response)


class CreateReservation(object):
    def __init__(self, json_data):
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.contact_phone = json_data.get('ContactPhone')
        self.contact_emails = json_data.get('ContactEmails')
        self.confirm_till = get_datetime(json_data.get('ConfirmTill'))
        self.customers = get_array(json_data.get('Customers'), OrderCreateReservationCustomerResponse)
        self.reservation_results = get_array(json_data.get('ReservationResults'), ReservationResponse)

        self.json_data = json_data


class ProlongReservation(object):
    def __init__(self, json_data):
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.confirm_till = get_datetime(json_data.get('ConfirmTill'))

        self.json_data = json_data


class Confirm(object):
    def __init__(self, json_data):
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.customers = get_array(json_data.get('Customers'),  OrderCustomerResponse)
        self.confirm_results = get_array(json_data.get('ConfirmResults'), RailwayConfirmResponse)

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
        self.service_return_response = get_item(json_data.get('ServiceReturnResponse'), RailwayReturnAmountResponse)

        self.json_data = json_data


class AutoReturn(object):
    def __init__(self, json_data):
        self.service_return_response = get_item(json_data.get('ServiceReturnResponse'), RailwayAutoReturnResponse)

        self.json_data = json_data


class AddUpsale(object):
    def __init__(self, json_data):
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.upsale_results = get_array(json_data.get('UpsaleResults'), CustomerUpsaleOperationResult)

        self.json_data = json_data


class RefuseUpsale(object):
    def __init__(self, json_data):
        self.order_id = get_item(json_data.get('OrderId'), int)

        self.json_data = json_data


class UpdateBlanks(object):
    def __init__(self, json_data):
        self.blanks = get_array(json_data.get('Blanks'), RailwayBlankInfo)
        self.is_modified = get_bool_item(json_data.get('IsModified'))

        self.json_data = json_data


class ElectronicRegistration(object):
    def __init__(self, json_data):
        self.expiration_electronic_registration_date_time = get_datetime(json_data.get('ExpirationElectronicRegistrationDateTime'))
        self.blanks = get_array(json_data.get('Blanks'), RailwayBlankInfo)

        self.json_data = json_data


class MealOption(object):
    def __init__(self, json_data):
        self.meal_option_code = json_data.get('MealOptionCode')

        self.json_data = json_data


class BlankAsHtml(object):
    def __init__(self, data):
        self.__data = data

    @property
    def html(self):
        return self.__data.text
