from ..utils import get_array, get_item, get_datetime, get_datetime_array


class Discount(object):
    def __init__(self, json_data):
        self.discount_type = json_data.get('DiscountType', None)
        self.description = json_data.get('Description', None)

        self.json_data = json_data


class FeeCalculation(object):
    def __init__(self, json_data):
        self.charge = json_data.get('Charge', None)
        self.profit = json_data.get('Profit', None)

        self.json_data = json_data


class StationClarifying(object):
    def __init__(self, json_data):
        self.station_type = StationType(json_data.get('StationType', None))

        self.json_data = json_data


class StationType(object):
    def __init__(self, json_data):
        self.origin = json_data.get('Origin', None)
        self.destination = [StationInfo(station_info) for station_info in json_data.get('Destination', None)]

        self.json_data = json_data


class StationInfo(object):
    def __init__(self, json_data):
        self.station_name = json_data.get('StationName', None)
        self.station_code = json_data.get('StationCode', None)

        self.json_data = json_data


class TrainPriceInfo(object):
    def __init__(self, json_data):
        self.has_electronic_registration = json_data.get('HasElectronicRegistration', None)
        self.has_dynamic_pricing_cars = json_data.get('HasDynamicPricingCars', None)
        self.has_two_storey_cars = json_data.get('HasTwoStoreyCars', None)
        self.carriers = json_data.get('Carriers', None)
        self.car_groups = get_array(json_data.get('CarGroups', None), CarGroupPriceInfo)
        self.id = json_data.get('Id', None)
        self.train_number = json_data.get('TrainNumber', None)
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute', None)
        self.display_train_number = json_data.get('DisplayTrainNumber', None)
        self.train_description = json_data.get('TrainDescription', None)
        self.train_name = json_data.get('TrainName', None)
        self.transport_type = json_data.get('TransportType', None)
        self.origin_name = json_data.get('OriginName', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_name = json_data.get('DestinationName', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.destination_names = json_data.get('DestinationNames', None)
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime', None))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))
        self.arrival_date_times = get_datetime_array(json_data.get('ArrivalDateTimes', None))
        self.departure_date_from_forming_station = get_datetime(json_data.get('DepartureDateFromFormingStation', None))
        self.departure_stop_time = json_data.get('DepartureStopTime', None)
        self.arrival_stop_time = json_data.get('ArrivalStopTime', None)
        self.trip_duration = json_data.get('TripDuration', None)
        self.trip_distance = json_data.get('TripDistance', None)
        self.is_suburban = json_data.get('IsSuburban', None)
        self.is_component = json_data.get('IsComponent', None)
        self.car_services = json_data.get('CarServices', None)
        self.is_sale_forbidden = json_data.get('IsSaleForbidden', None)

        self.json_data = json_data


class CarGroupPriceInfo(object):
    def __init__(self, json_data):
        self.car_type = json_data.get('CarType', None)
        self.car_type_name = json_data.get('CarTypeName', None)
        self.place_quantity = json_data.get('PlaceQuantity', None)
        self.lower_place_quantity = json_data.get('LowerPlaceQuantity', None)
        self.upper_place_quantity = json_data.get('UpperPlaceQuantity', None)
        self.lower_side_place_quantity = json_data.get('LowerSidePlaceQuantity', None)
        self.upper_side_place_quantity = json_data.get('UpperSidePlaceQuantity', None)
        self.male_place_quantity = json_data.get('MalePlaceQuantity', None)
        self.female_place_quantity = json_data.get('FemalePlaceQuantity', None)
        self.empty_cabin_quantity = json_data.get('EmptyCabinQuantity', None)
        self.mixed_cabin_quantity = json_data.get('MixedCabinQuantity', None)
        self.min_price = json_data.get('MinPrice', None)
        self.max_price = json_data.get('MaxPrice', None)
        self.carriers = json_data.get('Carriers', None)
        self.car_descriptions = json_data.get('CarDescriptions', None)
        self.service_classes = json_data.get('ServiceClasses', None)
        self.service_costs = json_data.get('ServiceCosts', None)
        self.is_bedding_selection_possible = json_data.get('IsBeddingSelectionPossible', None)
        self.has_electronic_registration = json_data.get('HasElectronicRegistration', None)
        self.has_gender_cabins = json_data.get('HasGenderCabins', None)
        self.has_place_numeration = json_data.get('HasPlaceNumeration', None)
        self.has_places_near_playground = json_data.get('HasPlacesNearPlayground', None)
        self.has_places_near_pets = json_data.get('HasPlacesNearPets', None)
        self.has_places_near_babies = json_data.get('HasPlacesNearBabies', None)
        self.discounts = get_array(json_data.get('Discounts', None), Discount)
        self.info_request_schema = json_data.get('InfoRequestSchema', None)
        self.total_place_quantity = json_data.get('TotalPlaceQuantity', None)
        self.place_reservation_types = json_data.get('PlaceReservationTypes', None)

        self.json_data = json_data


class CarPriceInfo(object):
    def __init__(self, json_data):
        self.car_type = json_data.get('CarType', None)
        self.car_sub_type = json_data.get('CarSubType', None)
        self.car_type_name = json_data.get('CarTypeName', None)
        self.car_number = json_data.get('CarNumber', None)
        self.service_class = json_data.get('ServiceClass', None)
        self.international_service_class = json_data.get('InternationalServiceClass', None)
        self.car_description = json_data.get('CarDescription', None)
        self.service_class_transcript = json_data.get('ServiceClassTranscript', None)
        self.free_places = json_data.get('FreePlaces', None)
        self.place_quantity = json_data.get('PlaceQuantity', None)
        self.is_two_storey = json_data.get('IsTwoStorey', None)
        self.services = json_data.get('Services', None)
        self.min_price = json_data.get('MinPrice', None)
        self.max_price = json_data.get('MaxPrice', None)
        self.service_cost = json_data.get('ServiceCost', None)
        self.place_reservation_type = json_data.get('PlaceReservationType', None)
        self.carrier = json_data.get('Carrier', None)
        self.has_gender_cabins = json_data.get('HasGenderCabins', None)
        self.rzhd_card_types = json_data.get('RzhdCardTypes', None)
        self.train_number = json_data.get('TrainNumber', None)
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))
        self.has_no_interchange = json_data.get('HasNoInterchange', None)
        self.has_place_numeration = json_data.get('HasPlaceNumeration', None)
        self.is_bedding_selection_possible = json_data.get('IsBeddingSelectionPossible', None)
        self.has_electronic_registration = json_data.get('HasElectronicRegistration', None)
        self.has_dynamic_pricing = json_data.get('HasDynamicPricing', None)
        self.has_places_near_babies = json_data.get('HasPlacesNearBabies', None)
        self.has_places_near_playground = json_data.get('HasPlacesNearPlayground', None)
        self.has_places_near_pets = json_data.get('HasPlacesNearPets', None)
        self.is_additional_passenger_allowed = json_data.get('IsAdditionalPassengerAllowed', None)
        self.is_child_tariff_type_allowed = json_data.get('IsChildTariffTypeAllowed', None)
        self.car_place_type = json_data.get('CarPlaceType', None)
        self.discounts = get_array(json_data.get('Discounts', None), Discount)
        self.is_sale_forbidden = json_data.get('IsSaleForbidden', None)
        self.is_three_hours_reservation_available = json_data.get('IsThreeHoursReservationAvailable', None)
        self.road = json_data.get('Road', None)
        self.passenger_specifying_rules = json_data.get('PassengerSpecifyingRules', None)

        self.json_data = json_data


class TrainInfo(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber', None)
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute', None)
        self.display_train_number = json_data.get('DisplayTrainNumber', None)
        self.train_description = json_data.get('TrainDescription', None)
        self.train_name = json_data.get('TrainName', None)
        self.transport_type = json_data.get('TransportType', None)
        self.origin_name = json_data.get('OriginName', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_name = json_data.get('DestinationName', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.destination_names = json_data.get('DestinationNames', None)
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime', None))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))
        self.arrival_date_times = get_datetime_array(json_data.get('ArrivalDateTimes', None))
        self.departure_date_from_forming_station = get_datetime(json_data.get('DepartureDateFromFormingStation', None))
        self.departure_stopTime = json_data.get('DepartureStopTime', None)
        self.arrivalStopTime = json_data.get('ArrivalStopTime', None)
        self.trip_duration = json_data.get('TripDuration', None)
        self.trip_distance = json_data.get('TripDistance', None)
        self.is_suburban = json_data.get('IsSuburban', None)
        self.is_component = json_data.get('IsComponent', None)
        self.car_services = json_data.get('CarServices', None)
        self.is_sale_forbidden = json_data.get('IsSaleForbidden', None)

        self.json_data = json_data


class ScheduleInfo(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber', None)
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute', None)
        self.train_name = json_data.get('TrainName', None)
        self.origin_name = json_data.get('OriginName', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_name = json_data.get('DestinationName', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.departure_time = json_data.get('DepartureTime', None)
        self.departure_stop_time = json_data.get('DepartureStopTime', None)
        self.arrival_time = json_data.get('ArrivalTime', None)
        self.arrival_stop_time = json_data.get('ArrivalStopTime', None)
        self.trip_duration = json_data.get('TripDuration', None)
        self.trip_distance = json_data.get('TripDistance', None)
        self.regularity = json_data.get('Regularity', None)
        self.start_sales_date_time = get_datetime(json_data.get('StartSalesDateTime', None))

        self.json_data = json_data


class TrainRouteRoute(object):
    def __init__(self, json_data):
        self.name = json_data.get('Name', None)
        self.origin_name = json_data.get('OriginName', None)
        self.destination_name = json_data.get('DestinationName', None)
        self.route_stops = get_array(json_data.get('RouteStops', None), RouteStopInfo)

        self.json_data = json_data


class RouteStopInfo(object):
    def __init__(self, json_data):
        self.station_name = json_data.get('StationName', None)
        self.city_name = json_data.get('CityName', None)
        self.departure_time = json_data.get('DepartureTime', None)
        self.arrival_time = json_data.get('ArrivalTime', None)
        self.route_stop_type = json_data.get('RouteStopType', None)
        self.stop_duration = json_data.get('StopDuration', None)
        self.time_description = json_data.get('TimeDescription', None)
        self.station_time_description = json_data.get('StationTimeDescription', None)

        self.json_data = json_data


class Route(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime', None))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))
        self.travel_time = json_data.get('TravelTime', None)
        self.change_time = json_data.get('ChangeTime', None)
        self.route_parts = get_array(json_data.get('RouteParts', None), RoutePart)

        self.json_data = json_data


class RoutePart(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber', None)
        self.origin_city_code = json_data.get('OriginCityCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_city_code = json_data.get('DestinationCityCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime', None))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime', None))

        self.json_data = json_data


class TrainPricingResponse(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.trains = get_array(json_data.get('Trains', None), TrainPriceInfo)
        self.departure_time_description = json_data.get('DepartureTimeDescription', None)
        self.arrival_time_description = json_data.get('ArrivalTimeDescription', None)
        self.is_from_ukrain = json_data.get('IsFromUkrain', None)
        self.client_fee_calculation = json_data.get('ClientFeeCalculation', None)
        self.agent_fee_calculation = json_data.get('AgentFeeCalculation', None)
        self.not_all_trains_returned = json_data.get('NotAllTrainsReturned', None)

        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation', None), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation', None), FeeCalculation)
        self.not_all_trains_returned = json_data.get('NotAllTrainsReturned', None)
        self.station_clarifying = get_item(json_data.get('StationClarifying', None), StationClarifying)
        self.booking_system = json_data.get('BookingSystem', None)
        self.id = json_data.get('Id', None)
        self.route_policy = json_data.get('RoutePolicy', None)

        self.json_data = json_data


class RouteReferenced(object):
    def __init__(self, json_data):
        self.route_parts = get_array(json_data.get('RouteParts', None), RoutePartReferenced)

        self.json_data = json_data


class RoutePartReferenced(object):
    def __init__(self, json_data):
        self.pricing_id = json_data.get('PricingId', None)
        self.train_id = json_data.get('TrainId', None)

        self.json_data = json_data


class MealOption(object):
    def __init__(self, json_data):
        self.meal_option_code = json_data.get('MealOptionCode', None)
        self.description = json_data.get('Description', None)

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
