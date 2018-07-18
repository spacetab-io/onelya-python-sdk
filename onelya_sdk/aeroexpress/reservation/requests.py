from datetime import datetime
from onelya_sdk import utils
from onelya_sdk.wrapper.types import (RailwayPassengerCategory, PreferredAdultTariffType, CarType, CarStorey,
                                      RzhdCardTypes, CabinGenderKind, CabinPlaceDemands, ProviderPaymentForm,
                                      AdditionalPlaceRequirements, DocumentType, Sex)


class AeroexpressPassengerRequest(object):
    def __init__(self, order_customer_index):
        self.order_customer_index = order_customer_index


class OrderFullCustomerRequest(object):
    def __init__(self, document_number: str, document_type: DocumentType, first_name: str, last_name: str, sex: Sex,
                 index: int, middle_name: str=None, document_valid_till: datetime=None, citizenship_code: str=None,
                 birth_place: str=None, birthday: datetime=datetime.fromtimestamp(0)):
        self.type = 'ApiContracts.Order.V1.Reservation.OrderFullCustomerRequest, ApiContracts'
        self.document_number = document_number
        self.document_type = document_type
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.index = index
        self.middle_name = middle_name if middle_name is not None else '-'
        self.document_valid_till = document_valid_till
        self.citizenship_code = citizenship_code
        self.birth_place = birth_place
        self.birthday = birthday

        self.json_data = {
            'type': self.type,
            'document_number': self.document_number,
            'document_type': self.document_type,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'sex': self.sex,
            'index': self.index,
            'middle_name': self.middle_name,
            'document_valid_till': utils.str_datetime(self.document_valid_till),
            'citizenship_code': self.citizenship_code,
            'birth_place': self.birth_place,
            'birthday': utils.str_datetime(self.birthday)
        }


class AeroexpressReservationRequest(object):
    def __init__(self, tariff_id: str, departure_date: datetime, passengers: 'list of int', index: int,
                 schedule_id: str=None, provider_payment_form: ProviderPaymentForm=None, agent_reference_id: str=None,
                 agent_payment_id: str=None):
        self.type = 'ApiContracts.Aeroexpress.V1.Messages.Reservation.AeroexpressReservationRequest, ApiContracts'
        self.tariff_id = tariff_id
        self.departure_date = departure_date
        self.passengers = utils.get_array(passengers, AeroexpressPassengerRequest)
        self.index = index
        self.schedule_id = schedule_id
        self.provider_payment_form = provider_payment_form
        self.agent_reference_id = agent_reference_id
        self.agent_payment_id = agent_payment_id

        self.json_data = {
            'type': self.type,
            'tariff_id': self.tariff_id,
            'departure_date': utils.str_datetime(self.departure_date),
            'passengers': [item.order_customer_index for item in self.passengers],
            'index': self.index,
            'schedule_id': self.schedule_id,
            'provider_payment_form': self.provider_payment_form,
            'agent_reference_id': self.agent_reference_id,
            'agent_payment_id': self.agent_payment_id
        }


class OrderCustomerDocuments(object):
    def __init__(self, order_customer_id: int=None, document_number: str=None, document_type: DocumentType=None,
                 document_valid_till: datetime=None, citizenship: str=None):
        self.order_customer_id = order_customer_id
        self.document_number = document_number
        self.document_type = document_type
        self.document_valid_till = document_valid_till
        self.citizenship = citizenship


class AeroexpressAutoReturnRequest(object):
    def __init__(self, order_item_id: int, agent_reference_id: str=None):
        self.type = 'ApiContracts.Aeroexpress.V1.Messages.Return.AeroexpressAutoReturnRequest, ApiContracts'
        self.order_item_id = order_item_id
        self.agent_reference_id = agent_reference_id


class ProductRequest(object):
    def __init__(self, package: str):
        self.type = 'ApiContracts.Insurance.V1.Products.Travel.AddUpsale.AviaAddUpsaleRequest, ApiContracts'
        self.package = package
