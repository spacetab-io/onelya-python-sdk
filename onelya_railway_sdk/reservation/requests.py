from datetime import datetime
from onelya_railway_sdk.wrapper.types import (RailwayPassengerCategory, PreferredAdultTariffType, CarType, CarStorey,
                                              RzhdCardTypes, CabinGenderKind, CabinPlaceDemands, ProviderPaymentForm,
                                              AdditionalPlaceRequirements, DocumentType, Sex)


class RailwayPassengerRequest(object):
    def __init__(self, category: RailwayPassengerCategory, order_customer_index: int,
                 preferred_adult_tariff_type: PreferredAdultTariffType=PreferredAdultTariffType.FULL,
                 railway_bonus_cards: 'list of RailwayBonusCardInfo'=None, is_invalid: bool=None):
        self.category = category
        self.order_customer_index = order_customer_index
        self.preferred_adult_tariff_type = preferred_adult_tariff_type
        self.railway_bonus_cards = railway_bonus_cards
        self.is_invalid = is_invalid


class RailwayBonusCardInfo(object):
    def __init__(self, card_number: str, car_type: RzhdCardTypes=None):
        self.card_number = card_number
        self.car_type = car_type


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
        self.middle_name = middle_name
        self.document_valid_till = document_valid_till
        self.citizenship_code = citizenship_code
        self.birth_place = birth_place
        self.birthday = birthday


class RailwayReservationRequest(object):
    def __init__(self, origin_code: str, destination_code: str, departure_date: datetime, train_number: str,
                 car_type: CarType, passengers: 'list of RailwayPassengerRequest', index: int, car_number: str=None,
                 lower_place_quantity: int=None, upper_place_quantity: int=None, cabin_gender_kind: CabinGenderKind=None,
                 car_storey: CarStorey=None, place_range: "tuple (min: int, max: int))"=None, bedding: bool=None,
                 cabin_place_demands: CabinPlaceDemands=None, set_electronic_registration: bool=None,
                 service_class: str=None, additional_place_requirements: AdditionalPlaceRequirements=None,
                 international_service_class: str=None, provider_payment_form: ProviderPaymentForm=None,
                 agent_reference_id: str=None, agent_payment_id: str=None):
        self.type = 'ApiContracts.Railway.V1.Messages.Reservation.RailwayReservationRequest, ApiContracts'
        self.origin_code = origin_code
        self.destination_code = destination_code
        self.departure_date = departure_date
        self.train_number = train_number
        self.car_type = car_type
        self.passengers = passengers
        self.index = index
        self.car_number = car_number
        self.lower_place_quantity = lower_place_quantity
        self.upper_place_quantity = upper_place_quantity
        self.cabin_gender_kind = cabin_gender_kind
        self.car_storey = car_storey
        self.place_range = None if place_range is None else {'From': place_range[0], 'To': place_range[1]}
        self.cabin_place_demands = cabin_place_demands
        self.set_electronic_registration = set_electronic_registration
        self.bedding = bedding
        self.service_class = service_class
        self.international_service_class = international_service_class
        self.additional_place_requirements = additional_place_requirements
        self.provider_payment_form = provider_payment_form
        self.agent_reference_id = agent_reference_id
        self.agent_payment_id = agent_payment_id


class OrderCustomerDocuments(object):
    def __init__(self, order_customer_id: int=None, document_number: str=None, document_type: DocumentType=None,
                 document_valid_till: datetime=None, citizenship: str=None):
        self.order_customer_id = order_customer_id
        self.document_number = document_number
        self.document_type = document_type
        self.document_valid_till = document_valid_till
        self.citizenship = citizenship


class ServiceReturnAmountRequest(object):
    def __init__(self, check_document_number: str, order_item_id: int, order_item_blank_ids: 'list of int'=None):
        self.type = 'ApiContracts.Railway.V1.Messages.Return.RailwayReturnAmountRequest, ApiContracts'
        self.check_document_number = check_document_number
        self.order_item_id = order_item_id
        self.order_item_blank_ids = order_item_blank_ids
