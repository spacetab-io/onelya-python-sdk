from datetime import datetime
from ..utils import get_datetime, get_item, get_array
from onelya_railway_sdk.wrapper import FeeCalculation
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


class OrderCreateReservationCustomerResponse(object):
    def __init__(self, json_data):
        self.index = json_data.get('Index', None)
        self.order_customer_id = json_data.get('OrderCustomerId', None)
        self.first_name = json_data.get('FirstName', None)
        self.middle_name = json_data.get('MiddleName', None)
        self.last_name = json_data.get('LastName', None)
        self.sex = json_data.get('Sex', None)
        self.birth_date = json_data.get('BirthDate', None)
        self.document_number = json_data.get('DocumentNumber', None)
        self.document_valid_till = json_data.get('DocumentValidTill', None)
        self.document_type = json_data.get('DocumentType', None)
        self.citizenship_code = json_data.get('CitizenshipCode', None)
        self.birth_place = json_data.get('BirthPlace', None)

        self.json_data = json_data


class RateValue(object):
    def __init__(self, json_data):
        self.rate = json_data.get('Rate', None)
        self.value = json_data.get('Value', None)

        self.json_data = json_data


class TicketTariffInfo(object):
    def __init__(self, json_data):
        self.tariff_type = json_data.get('TariffType', None)
        self.tariff_name = json_data.get('TariffName', None)

        self.json_data = json_data


class RailwayReservationBlankResponse(object):
    def __init__(self, json_data):
        self.order_item_blank_id = json_data.get('OrderItemBlankId', None)
        self.amount = json_data.get('Amount', None)
        self.number = json_data.get('Number', None)
        self.tariff_type = json_data.get('TariffType', None)
        self.is_meal_option_possible = json_data.get('IsMealOptionPossible', None)
        self.vat_rate_values = get_array(json_data.get('VatRateValues', None), RateValue)
        self.base_fare = json_data.get('BaseFare', None)
        self.additional_price = json_data.get('AdditionalPrice', None)
        self.tariff_info = get_item(json_data.get('TariffInfo', None), TicketTariffInfo)
        self.service_price = json_data.get('ServicePrice', None)

        self.json_data = json_data


class PlaceWithType(object):
    def __init__(self, json_data):
        self.number = json_data.get('Number', None)
        self.type = json_data.get('Type', None)

        self.json_data = json_data


class RailwayPassengerResponse(object):
    def __init__(self, json_data):
        self.category = json_data.get('Category', None)
        self.places = json_data.get('Places', None)
        self.place_tiers = json_data.get('PlaceTiers', None)
        self.places_with_type = get_item(json_data.get('PlacesWithType', None), PlaceWithType)
        self.tariff_type = json_data.get('TariffType', None)
        self.first_name = json_data.get('FirstName', None)
        self.middle_name = json_data.get('MiddleName', None)
        self.last_name = json_data.get('LastName', None)
        self.birth_date = json_data.get('BirthDate', None)
        self.sex = json_data.get('Sex', None)
        self.citizenship = json_data.get('Citizenship', None)
        self.order_item_blank_id = json_data.get('OrderItemBlankId', None)
        self.order_customer_id = json_data.get('OrderCustomerId', None)
        self.order_customer_reference_index = json_data.get('OrderCustomerReferenceIndex', None)
        self.amount = json_data.get('Amount', None)
        self.fare = json_data.get('Fare', None)
        self.tax = json_data.get('Tax', None)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation', None), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation', None), FeeCalculation)

        self.json_data = json_data


class RailwayReservationResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type', None)
        self.blanks = get_array(json_data.get('Blanks', None), RailwayReservationBlankResponse)
        self.origin_station = json_data.get('OriginStation', None)
        self.destination_station = json_data.get('DestinationStation', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.train_number = json_data.get('TrainNumber', None)
        self.booking_train_number = json_data.get('BookingTrainNumber', None)
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute', None)
        self.car_number = json_data.get('CarNumber', None)
        self.service_class = json_data.get('ServiceClass', None)
        self.international_service_class = json_data.get('InternationalServiceClass', None)
        self.time_description = json_data.get('TimeDescription', None)
        self.is_print_ticket_possible = json_data.get('IsPrintTicketPossible', None)
        self.nearest_ticket_print_stations = json_data.get('NearestTicketPrintStations', None)
        self.carrier = json_data.get('Carrier', None)
        self.carrier_code = json_data.get('CarrierCode', None)
        self.carrier_tin = json_data.get('CarrierTin', None)
        self.country_code = json_data.get('CountryCode', None)
        self.is_meal_option_possible = json_data.get('IsMealOptionPossible', None)
        self.meal_group = json_data.get('MealGroup', None)
        self.booking_system = json_data.get('BookingSystem', None)
        self.is_three_hours_reservation_available = json_data.get('IsThreeHoursReservationAvailable', None)
        self.trip_duration = json_data.get('TripDuration', None)
        self.train_description = json_data.get('TrainDescription', None)
        self.car_description = json_data.get('CarDescription', None)
        self.is_suburban = json_data.get('IsSuburban', None)
        self.passengers = get_array(json_data.get('Passengers', None), RailwayPassengerResponse)
        self.index = json_data.get('Index', None)
        self.order_item_id = json_data.get('OrderItemId', None)
        self.agent_reference_id = json_data.get('AgentReferenceId', None)
        self.amount = json_data.get('Amount', None)
        self.fare = json_data.get('Fare', None)
        self.tax = json_data.get('Tax', None)
        self.reservation_number = json_data.get('ReservationNumber', None)
        self.confirm_till = json_data.get('ConfirmTill', None)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation', None), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation', None), FeeCalculation)
        self.error_result = json_data.get('ErrorResult', None)
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime', None))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))

        self.json_data = json_data


class CreateReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.amount = json_data.get('Amount', None)
        self.confirm_till = get_datetime(json_data.get('ConfirmTill', None))
        self.customers = get_array(json_data.get('Customers', None), OrderCreateReservationCustomerResponse)
        self.reservation_results = get_array(json_data.get('ReservationResults', None), RailwayReservationResponse)

        self.json_data = json_data
