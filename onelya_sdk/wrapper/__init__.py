from ..utils import get_array, get_item, get_datetime, get_datetime_array, get_bool_item, get_array_from_str


class Discount(object):
    def __init__(self, json_data):
        self.discount_type = json_data.get('DiscountType')
        self.description = json_data.get('Description')

        self.json_data = json_data


class FeeCalculation(object):
    def __init__(self, json_data):
        self.charge = get_item(json_data.get('Charge'), float)
        self.profit = get_item(json_data.get('Profit'), float)

        self.json_data = json_data


class StationClarifying(object):
    def __init__(self, json_data):
        self.station_type = json_data.get('StationType')
        self.station_options = get_array(json_data.get('StationOptions'), StationInfo)

        self.json_data = json_data


class StationInfo(object):
    def __init__(self, json_data):
        self.station_name = json_data.get('StationName')
        self.station_code = json_data.get('StationCode')

        self.json_data = json_data


class TrainPriceInfo(object):
    def __init__(self, json_data):
        self.has_electronic_registration = get_bool_item(json_data.get('HasElectronicRegistration'))
        self.has_dynamic_pricing_cars = get_bool_item(json_data.get('HasDynamicPricingCars'))
        self.has_two_storey_cars = get_bool_item(json_data.get('HasTwoStoreyCars'))
        self.carriers = json_data.get('Carriers')
        self.car_groups = get_array(json_data.get('CarGroups'), CarGroupPriceInfo)
        self.id = get_item(json_data.get('Id'), int)
        self.train_number = json_data.get('TrainNumber')
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute')
        self.display_train_number = json_data.get('DisplayTrainNumber')
        self.train_description = json_data.get('TrainDescription')
        self.train_name = json_data.get('TrainName')
        self.transport_type = json_data.get('TransportType')
        self.origin_name = json_data.get('OriginName')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.destination_name = json_data.get('DestinationName')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.destination_names = json_data.get('DestinationNames')
        self.local_arrival_date_time = get_datetime(json_data.get('LocalArrivalDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.arrival_date_times = get_datetime_array(json_data.get('ArrivalDateTimes'))
        self.local_departure_date_time = get_datetime(json_data.get('LocalDepartureDateTime'))
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.departure_date_from_forming_station = get_datetime(json_data.get('DepartureDateFromFormingStation'))
        self.departure_stop_time = get_item(json_data.get('DepartureStopTime'), int)
        self.arrival_stop_time = get_item(json_data.get('ArrivalStopTime'), int)
        self.trip_duration = get_item(json_data.get('TripDuration'), int)
        self.trip_distance = get_item(json_data.get('TripDistance'), int)
        self.is_suburban = get_bool_item(json_data.get('IsSuburban'))
        self.is_component = get_bool_item(json_data.get('IsComponent'))
        self.car_services = json_data.get('CarServices')
        self.is_sale_forbidden = get_bool_item(json_data.get('IsSaleForbidden'))

        self.json_data = json_data


class CarGroupPriceInfo(object):
    def __init__(self, json_data):
        self.car_type = json_data.get('CarType')
        self.car_type_name = json_data.get('CarTypeName')
        self.place_quantity = get_item(json_data.get('PlaceQuantity'), int)
        self.lower_place_quantity = get_item(json_data.get('LowerPlaceQuantity'), int)
        self.upper_place_quantity = get_item(json_data.get('UpperPlaceQuantity'), int)
        self.lower_side_place_quantity = get_item(json_data.get('LowerSidePlaceQuantity'), int)
        self.upper_side_place_quantity = get_item(json_data.get('UpperSidePlaceQuantity'), int)
        self.male_place_quantity = get_item(json_data.get('MalePlaceQuantity'), int)
        self.female_place_quantity = get_item(json_data.get('FemalePlaceQuantity'), int)
        self.empty_cabin_quantity = get_item(json_data.get('EmptyCabinQuantity'), int)
        self.mixed_cabin_quantity = get_item(json_data.get('MixedCabinQuantity'), int)
        self.min_price = get_item(json_data.get('MinPrice'), float)
        self.max_price = get_item(json_data.get('MaxPrice'), float)
        self.carriers = json_data.get('Carriers')
        self.car_descriptions = json_data.get('CarDescriptions')
        self.service_classes = json_data.get('ServiceClasses')
        self.service_costs = get_array(json_data.get('ServiceCosts'), float)
        self.international_service_classes = json_data.get('InternationalServiceClasses')
        self.availability_indication = json_data.get('AvailabilityIndication')
        self.is_three_hours_reservation_available = get_bool_item(json_data.get('IsThreeHoursReservationAvailable'))
        self.is_deferred_payment_available = get_bool_item(json_data.get('IsDeferredPaymentAvailable'))
        self.is_meal_option_possible = get_bool_item(json_data.get('IsMealOptionPossible'))
        self.is_additional_meal_option_possible = get_bool_item(json_data.get('IsAdditionalMealOptionPossible'))
        self.is_transit_document_required = get_bool_item(json_data.get('IsTransitDocumentRequired'))
        self.is_bedding_selection_possible = get_bool_item(json_data.get('IsBeddingSelectionPossible'))
        self.is_sale_forbidden = get_bool_item(json_data.get('IsSaleForbidden'))
        self.has_electronic_registration = get_bool_item(json_data.get('HasElectronicRegistration'))
        self.has_gender_cabins = get_bool_item(json_data.get('HasGenderCabins'))
        self.has_place_numeration = get_bool_item(json_data.get('HasPlaceNumeration'))
        self.has_places_near_playground = get_bool_item(json_data.get('HasPlacesNearPlayground'))
        self.has_places_near_pets = get_bool_item(json_data.get('HasPlacesNearPets'))
        self.has_places_near_babies = get_bool_item(json_data.get('HasPlacesNearBabies'))
        self.discounts = get_array(json_data.get('Discounts'), Discount)
        self.info_request_schema = json_data.get('InfoRequestSchema')
        self.total_place_quantity = get_item(json_data.get('TotalPlaceQuantity'), int)
        self.place_reservation_types = json_data.get('PlaceReservationTypes')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class FreePlacesByCompartments(object):
    def __init__(self, json_data):
        self.compartment_number = json_data.get('CompartmentNumber')
        self.places = get_array_from_str(json_data.get('Places'))


class CarPriceInfo(object):
    def __init__(self, json_data):
        self.car_type = json_data.get('CarType')
        self.car_sub_type = json_data.get('CarSubType')
        self.car_type_name = json_data.get('CarTypeName')
        self.car_number = json_data.get('CarNumber')
        self.service_class = json_data.get('ServiceClass')
        self.international_service_class = json_data.get('InternationalServiceClass')
        self.car_description = json_data.get('CarDescription')
        self.service_class_transcript = json_data.get('ServiceClassTranscript')
        self.free_places = get_array_from_str(json_data.get('FreePlaces'))
        self.place_quantity = get_item(json_data.get('PlaceQuantity'), int)
        self.is_two_storey = json_data.get('IsTwoStorey')
        self.services = json_data.get('Services')
        self.min_price = get_item(json_data.get('MinPrice'), float)
        self.max_price = get_item(json_data.get('MaxPrice'), float)
        self.service_cost = get_item(json_data.get('ServiceCost'), float)
        self.free_places_by_compartments = get_array(json_data.get('FreePlacesByCompartments'), FreePlacesByCompartments)
        self.place_reservation_type = json_data.get('PlaceReservationType')
        self.availability_indication = json_data.get('AvailabilityIndication')
        self.carrier = json_data.get('Carrier')
        self.has_gender_cabins = json_data.get('HasGenderCabins')
        self.rzhd_card_types = json_data.get('RzhdCardTypes')
        self.train_number = json_data.get('TrainNumber')
        self.local_arrival_date_time = get_datetime(json_data.get('LocalArrivalDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.has_no_interchange = get_bool_item(json_data.get('HasNoInterchange'))
        self.has_place_numeration = get_bool_item(json_data.get('HasPlaceNumeration'))
        self.is_bedding_selection_possible = get_bool_item(json_data.get('IsBeddingSelectionPossible'))
        self.has_electronic_registration = get_bool_item(json_data.get('HasElectronicRegistration'))
        self.has_dynamic_pricing = get_bool_item(json_data.get('HasDynamicPricing'))
        self.has_places_near_babies = get_bool_item(json_data.get('HasPlacesNearBabies'))
        self.has_places_near_playground = get_bool_item(json_data.get('HasPlacesNearPlayground'))
        self.has_places_near_pets = get_bool_item(json_data.get('HasPlacesNearPets'))
        self.is_additional_passenger_allowed = get_bool_item(json_data.get('IsAdditionalPassengerAllowed'))
        self.is_meal_option_possible = get_bool_item(json_data.get('IsMealOptionPossible'))
        self.is_additional_meal_option_possible = get_bool_item(json_data.get('IsAdditionalMealOptionPossible'))
        self.is_transit_document_required = get_bool_item(json_data.get('IsTransitDocumentRequired'))
        self.is_child_tariff_type_allowed = get_bool_item(json_data.get('IsChildTariffTypeAllowed'))
        self.car_place_type = json_data.get('CarPlaceType')
        self.discounts = get_array(json_data.get('Discounts'), Discount)
        self.is_sale_forbidden = get_bool_item(json_data.get('IsSaleForbidden'))
        self.is_three_hours_reservation_available = get_bool_item(json_data.get('IsThreeHoursReservationAvailable'))
        self.road = json_data.get('Road')
        self.passenger_specifying_rules = json_data.get('PassengerSpecifyingRules')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class TrainInfo(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber')
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute')
        self.display_train_number = json_data.get('DisplayTrainNumber')
        self.train_description = json_data.get('TrainDescription')
        self.train_name = json_data.get('TrainName')
        self.transport_type = json_data.get('TransportType')
        self.origin_name = json_data.get('OriginName')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.destination_name = json_data.get('DestinationName')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.destination_names = json_data.get('DestinationNames')
        self.local_departure_date_time = get_datetime(json_data.get('LocalDepartureDateTime'))
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.local_arrival_date_time = get_datetime(json_data.get('LocalArrivalDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.arrival_date_times = get_datetime_array(json_data.get('ArrivalDateTimes'))
        self.departure_date_from_forming_station = get_datetime(json_data.get('DepartureDateFromFormingStation'))
        self.departure_stop_time = get_item(json_data.get('DepartureStopTime'), int)
        self.arrival_stop_time = get_item(json_data.get('ArrivalStopTime'), int)
        self.trip_duration = get_item(json_data.get('TripDuration'), int)
        self.trip_distance = get_item(json_data.get('TripDistance'), int)
        self.is_suburban = get_bool_item(json_data.get('IsSuburban'))
        self.is_component = get_bool_item(json_data.get('IsComponent'))
        self.car_services = json_data.get('CarServices')
        self.is_sale_forbidden = get_bool_item(json_data.get('IsSaleForbidden'))

        self.json_data = json_data


class ScheduleInfo(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber')
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute')
        self.train_name = json_data.get('TrainName')
        self.origin_name = json_data.get('OriginName')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.destination_name = json_data.get('DestinationName')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.departure_time = json_data.get('DepartureTime')
        self.departure_stop_time = get_item(json_data.get('DepartureStopTime'), int)
        self.arrival_time = json_data.get('ArrivalTime')
        self.arrival_stop_time = get_item(json_data.get('ArrivalStopTime'), int)
        self.trip_duration = get_item(json_data.get('TripDuration'), int)
        self.trip_distance = get_item(json_data.get('TripDistance'), int)
        self.regularity = json_data.get('Regularity')
        self.start_sales_date_time = get_datetime(json_data.get('StartSalesDateTime'))

        self.json_data = json_data


class TrainRouteRoute(object):
    def __init__(self, json_data):
        self.name = json_data.get('Name')
        self.origin_name = json_data.get('OriginName')
        self.destination_name = json_data.get('DestinationName')
        self.route_stops = get_array(json_data.get('RouteStops'), RouteStopInfo)

        self.json_data = json_data


class RouteStopInfo(object):
    def __init__(self, json_data):
        self.station_name = json_data.get('StationName')
        self.city_name = json_data.get('CityName')
        self.departure_time = json_data.get('DepartureTime')
        self.arrival_time = json_data.get('ArrivalTime')
        self.route_stop_type = json_data.get('RouteStopType')
        self.stop_duration = get_item(json_data.get('StopDuration'), int)
        self.time_description = json_data.get('TimeDescription')
        self.station_time_description = json_data.get('StationTimeDescription')

        self.json_data = json_data


class Route(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.destination_code = json_data.get('DestinationCode')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.travel_time = get_item(json_data.get('TravelTime'), int)
        self.travel_distance = get_item(json_data.get('TravelDistance'), int)
        self.change_time = get_item(json_data.get('ChangeTime'), int)
        self.route_parts = get_array(json_data.get('RouteParts'), RoutePart)

        self.json_data = json_data


class RoutePart(object):
    def __init__(self, json_data):
        self.train_number = json_data.get('TrainNumber')
        self.origin_city_code = json_data.get('OriginCityCode')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.destination_city_code = json_data.get('DestinationCityCode')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))

        self.json_data = json_data


class TrainPricingResponse(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.origin_time_zone_difference = get_item(json_data.get('OriginTimeZoneDifference'), int)
        self.destination_code = json_data.get('DestinationCode')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.destination_time_zone_difference = get_item(json_data.get('DestinationTimeZoneDifference'), int)
        self.trains = get_array(json_data.get('Trains'), TrainPriceInfo)
        self.departure_time_description = json_data.get('DepartureTimeDescription')
        self.arrival_time_description = json_data.get('ArrivalTimeDescription')
        self.is_from_ukrain = get_bool_item(json_data.get('IsFromUkrain'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.not_all_trains_returned = get_bool_item(json_data.get('NotAllTrainsReturned'))
        self.station_clarifying = get_item(json_data.get('StationClarifying'), StationClarifying)
        self.booking_system = json_data.get('BookingSystem')
        self.id = get_item(json_data.get('Id'), int)
        self.route_policy = json_data.get('RoutePolicy')

        self.json_data = json_data


class RouteReferenced(object):
    def __init__(self, json_data):
        self.route_parts = get_array(json_data.get('RouteParts'), RoutePartReferenced)

        self.json_data = json_data


class RoutePartReferenced(object):
    def __init__(self, json_data):
        self.pricing_id = get_item(json_data.get('PricingId'), int)
        self.train_id = get_item(json_data.get('TrainId'), int)

        self.json_data = json_data


class AdditionalMealOption(object):
    def __init__(self, json_data):
        self.amount = get_item(json_data.get('Amount'), float)
        self.price_per_unit = get_item(json_data.get('PricePerUnit'), float)
        self.quantity = get_item(json_data.get('Quantity'), int)
        self.meal_time = json_data.get('MealTime')
        self.meal_name = json_data.get('MealName')
        self.meal_option_code = json_data.get('MealOptionCode')
        self.description = json_data.get('Description')

        self.json_data = json_data


class MealOption(object):
    def __init__(self, json_data):
        self.meal_option_code = json_data.get('MealOptionCode')
        self.description = json_data.get('Description')
        self.meal_type = json_data.get('MealType')

        self.json_data = json_data


class PlaceWithType(object):
    def __init__(self, json_data):
        self.number = json_data.get('Number')
        self.type = json_data.get('Type')

        self.json_data = json_data


class PassengerResponse(object):
    def __init__(self, json_data):
        self.category = json_data.get('Category')
        self.places = get_array_from_str(json_data.get('Places'))
        self.place_tiers = get_array_from_str(json_data.get('PlaceTiers'))
        self.places_with_type = get_array(json_data.get('PlacesWithType'), PlaceWithType)
        self.tariff_type = json_data.get('TariffType')
        self.first_name = json_data.get('FirstName')
        self.middle_name = json_data.get('MiddleName')
        self.last_name = json_data.get('LastName')
        self.birthday = get_datetime(json_data.get('BirthDay'))
        self.sex = json_data.get('Sex')
        self.citizenship = json_data.get('Citizenship')
        self.order_item_blank_id = get_item(json_data.get('OrderItemBlankId'), int)
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.order_customer_reference_index = get_item(json_data.get('OrderCustomerReferenceIndex'), int)
        self.amount = json_data.get('Amount')
        self.fare = json_data.get('Fare')
        self.tax = json_data.get('Tax')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class RateValue(object):
    def __init__(self, json_data):
        self.rate = get_item(json_data.get('Rate'), float)
        self.value = get_item(json_data.get('Value'), float)

        self.json_data = json_data


class TicketTariffInfo(object):
    def __init__(self, json_data):
        self.tariff_type = json_data.get('TariffType')
        self.tariff_name = json_data.get('TariffName')

        self.json_data = json_data


class PrepaidMealInfo(object):
    def __init__(self, json_data):
        self.meal_option_code = json_data.get('MealOptionCode')
        self.meal_name = json_data.get('MealName')
        self.description = json_data.get('Description')

        self.json_data = json_data


class ReservationBlankResponse(object):
    def __init__(self, json_data):
        self.order_item_blank_id = get_item(json_data.get('OrderItemBlankId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.number = json_data.get('Number')
        self.tariff_type = json_data.get('TariffType')
        self.is_meal_option_possible = get_bool_item(json_data.get('IsMealOptionPossible'))
        self.vat_rate_values = get_array(json_data.get('VatRateValues'), RateValue)
        self.base_fare = get_item(json_data.get('BaseFare'), float)
        self.additional_price = get_item(json_data.get('AdditionalPrice'), float)
        self.tariff_info = get_item(json_data.get('TariffInfo'), TicketTariffInfo)
        self.tariff_additional_info = json_data.get('TariffAdditionalInfo')
        self.prepaid_meal_info = get_item(json_data.get('PrepaidMealInfo'), PrepaidMealInfo)
        self.service_price = get_item(json_data.get('ServicePrice'), float)

        self.json_data = json_data


class ReservationResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.origin_station = json_data.get('OriginStation')
        self.origin_station_code = json_data.get('OriginStationCode')
        self.origin_time_zone_difference = get_item(json_data.get('OriginTimeZoneDifference'), int)
        self.destination_station = json_data.get('DestinationStation')
        self.destination_station_code = json_data.get('DestinationStationCode')
        self.destination_time_zone_difference = get_item(json_data.get('DestinationTimeZoneDifference'), int)
        self.blanks = get_array(json_data.get('Blanks'), ReservationBlankResponse)
        self.train_number = json_data.get('TrainNumber')
        self.booking_train_number = json_data.get('BookingTrainNumber')
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute')
        self.car_number = json_data.get('CarNumber')
        self.car_type = json_data.get('CarType')
        self.lower_place_quantity = json_data.get('LowerPlaceQuantity')
        self.upper_place_quantity = json_data.get('UpperPlaceQuantity')
        self.service_class = json_data.get('ServiceClass')
        self.international_service_class = json_data.get('InternationalServiceClass')
        self.time_description = json_data.get('TimeDescription')
        self.is_print_ticket_possible = get_bool_item(json_data.get('IsPrintTicketPossible'))
        self.nearest_ticket_print_stations = json_data.get('NearestTicketPrintStations')
        self.carrier = json_data.get('Carrier')
        self.carrier_code = json_data.get('CarrierCode')
        self.carrier_tin = json_data.get('CarrierTin')
        self.country_code = json_data.get('CountryCode')
        self.is_meal_option_possible = get_bool_item(json_data.get('IsMealOptionPossible'))
        self.is_additional_meal_option_possible = get_bool_item(json_data.get('IsAdditionalMealOptionPossible'))
        self.meal_group = json_data.get('MealGroup')
        self.booking_system = json_data.get('BookingSystem')
        self.is_three_hours_reservation_available = json_data.get('IsThreeHoursReservationAvailable')
        self.trip_duration = get_item(json_data.get('TripDuration'), int)
        self.train_description = json_data.get('TrainDescription')
        self.car_description = json_data.get('CarDescription')
        self.is_suburban = get_bool_item(json_data.get('IsSuburban'))
        self.cabin_gender_description = json_data.get('CabinGenderDescription')
        self.is_only_full_return_possible = json_data.get('IsOnlyFullReturnPossible')
        self.passengers = get_array(json_data.get('Passengers'), PassengerResponse)
        self.index = get_item(json_data.get('Index'), int)
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.amount = get_item(json_data.get('Amount'), float)
        self.fare = get_item(json_data.get('Fare'), float)
        self.tax = get_item(json_data.get('Tax'), float)
        self.reservation_number = json_data.get('ReservationNumber')
        self.confirm_till = get_datetime(json_data.get('ConfirmTill'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.error_result = json_data.get('ErrorResult')

        self.json_data = json_data


class OrderCreateReservationCustomerResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.index = get_item(json_data.get('Index'), int)
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.first_name = json_data.get('FirstName')
        self.middle_name = json_data.get('MiddleName')
        self.last_name = json_data.get('LastName')
        self.sex = json_data.get('Sex')
        self.birth_date = get_datetime(json_data.get('BirthDate'))
        self.document_number = json_data.get('DocumentNumber')
        self.document_valid_till = get_datetime(json_data.get('DocumentValidTill'))
        self.document_type = json_data.get('DocumentType')
        self.citizenship_code = json_data.get('CitizenshipCode')
        self.birth_place = json_data.get('BirthPlace')
        self.birthday = get_datetime(json_data.get('Birthday'))

        self.json_data = json_data


class OrderCustomerResponse(object):
    def __init__(self, json_data):
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.first_name = json_data.get('FirstName')
        self.middle_name = json_data.get('MiddleName')
        self.last_name = json_data.get('LastName')
        self.sex = json_data.get('Sex')
        self.birth_date = get_datetime(json_data.get('BirthDate'))
        self.document_number = json_data.get('DocumentNumber')
        self.document_valid_till = get_datetime(json_data.get('DocumentValidTill'))
        self.document_type = json_data.get('DocumentType')
        self.citizenship_code = json_data.get('CitizenshipCode')
        self.birth_place = json_data.get('BirthPlace')

        self.json_data = json_data


class RailwayBlankInfo(object):
    def __init__(self, json_data):
        self.order_item_blank_id = get_item(json_data.get('OrderItemBlankId'), int)
        self.number = json_data.get('Number')
        self.blank_status = json_data.get('BlankStatus')
        self.pending_electronic_registration = json_data.get('PendingElectronicRegistration')
        self.sign_sequence = json_data.get('sign_sequence')

        self.json_data = json_data


class OrderItemCustomerResponseBase(object):
    def __init__(self, json_data):
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.fare = get_item(json_data.get('Fare'), float)
        self.tax = get_item(json_data.get('Tax'), float)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class ApiErrorResult(object):
    def __init__(self, json_data):
        self.code = json_data.get('Code')
        self.message = json_data.get('Message')
        self.message_params = json_data.get('MessageParams')

        self.json_data = json_data


class RailwayConfirmResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.reservation_number = json_data.get('ReservationNumber')
        self.blanks = get_array(json_data.get('Blanks'), RailwayBlankInfo)
        self.expiration_electronic_registration_date_time = get_datetime(json_data.get('ExpirationElectronicRegistrationDateTime'))
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.fare = get_item(json_data.get('Fare'), float)
        self.tax = get_item(json_data.get('Tax'), float)
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.void_till = get_datetime(json_data.get('VoidTill'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.order_item_customers = get_array(json_data.get('OrderItemCustomers'), OrderItemCustomerResponseBase)
        self.warnings = get_array(json_data.get('Warnings'), ApiErrorResult)
        self.error_result = get_item(json_data.get('ErrorResult'), ApiErrorResult)

        self.json_data = json_data


class RailwayReturnBlankResponse(object):
    def __init__(self, json_data):
        self.purchase_order_item_blank_id = get_item(json_data.get('PurchaseOrderItemBlankId'), int)
        self.return_order_item_blank_id = get_item(json_data.get('ReturnOrderItemBlankId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.penalty = get_item(json_data.get('Penalty'), float)
        self.vat_rate_values = get_array(json_data.get('VatRateValues'), RateValue)
        self.service_price = get_item(json_data.get('ServicePrice'), float)

        self.json_data = json_data


class RailwayReturnAmountResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.blanks = get_array(json_data.get('Blanks'), RailwayReturnBlankResponse)
        self.amount = get_item(json_data.get('Amount'), float)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class RailwayAutoReturnResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.blanks = get_array(json_data.get('Blanks'), RailwayReturnBlankResponse)
        self.amount = get_item(json_data.get('Amount'), float)
        self.fare = get_item(json_data.get('Fare'), float)
        self.tax = get_item(json_data.get('Tax'), float)
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.return_order_item_id = get_item(json_data.get('ReturnOrderItemId'), int)
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class OrderCustomerInfo(object):
    def __init__(self, json_data):
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.first_name = json_data.get('FirstName')
        self.middle_name = json_data.get('MiddleName')
        self.last_name = json_data.get('LastName')
        self.sex = json_data.get('Sex')
        self.birth_date = get_datetime(json_data.get('BirthDate'))
        self.document_number = json_data.get('DocumentNumber')
        self.document_valid_till = get_datetime(json_data.get('DocumentValidTill'))
        self.document_type = json_data.get('DocumentType')
        self.citizenship_code = json_data.get('CitizenshipCode')

        self.json_data = json_data


class RailwayOrderItemCustomerInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.order_item_blank_id = json_data.get('OrderItemBlankId')
        self.places = get_array_from_str(json_data.get('Places'))
        self.place_quantity = json_data.get('PlaceQuantity')
        self.transit_document = json_data.get('TransitDocument')
        self.category = json_data.get('Category')
        self.order_customer_id = json_data.get('OrderCustomerId')
        self.order_item_customer_id = json_data.get('OrderItemCustomerId')
        self.amount = json_data.get('Amount')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class RailwayOrderItemBlankInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.voucher_number = json_data.get('VoucherNumber')
        self.base_fare = json_data.get('BaseFare')
        self.additional_price = json_data.get('AdditionalPrice')
        self.service_price = json_data.get('ServicePrice')
        self.vat_rate_values = get_array(json_data.get('VatRateValues'), RateValue)
        self.tariff_type = json_data.get('TariffType')
        self.blank_status = json_data.get('BlankStatus')
        self.is_electronic_registration_set = json_data.get('IsElectronicRegistrationSet')
        self.is_meal_option_possible = json_data.get('IsMealOptionPossible')
        self.pending_electronic_registration = json_data.get('PendingElectronicRegistration')
        self.electronic_registration_set_date_time = get_datetime(json_data.get('ElectronicRegistrationSetDateTime'))
        self.sign_sequence = json_data.get('SignSequence')
        self.tariff_info = get_item(json_data.get('TariffInfo'), TicketTariffInfo)
        self.prepaid_meal_info = get_item(json_data.get('PrepaidMealInfo'), PrepaidMealInfo)
        self.transit_permission_approval_status = json_data.get('TransitPermissionApprovalStatus')
        self.place_quantity = json_data.get('PlaceQuantity')
        self.order_item_blank_id = json_data.get('OrderItemBlankId')
        self.previous_order_item_blank_id = json_data.get('PreviousOrderItemBlankId')
        self.blank_number = json_data.get('BlankNumber')
        self.amount = json_data.get('Amount')

        self.json_data = json_data


class RailwayFullOrderItemInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.service_type = json_data.get('ServiceType')
        self.place_quantity = get_item(json_data.get('PlaceQuantity'), int)
        self.origin_station_name = json_data.get('OriginStationName')
        self.origin_time_zone_difference = get_item(json_data.get('OriginTimeZoneDifference'), int)
        self.destination_station_name = json_data.get('DestinationStationName')
        self.destination_time_zone_difference = get_item(json_data.get('DestinationTimeZoneDifference'), int)
        self.train_number = json_data.get('TrainNumber')
        self.booking_train_number = json_data.get('BookingTrainNumber')
        self.train_number_to_get_route = json_data.get('TrainNumberToGetRoute')
        self.car_number = json_data.get('CarNumber')
        self.car_type = json_data.get('CarType')
        self.electronic_registration_expiration_date_time = get_datetime(json_data.get('ElectronicRegistrationExpirationDateTime'))
        self.place_reservation_type = json_data.get('PlaceReservationType')
        self.service_class = json_data.get('ServiceClass')
        self.additional_information = json_data.get('AdditionalInformation')
        self.carrier_description = json_data.get('CarrierDescription')
        self.is_only_full_return_possible = json_data.get('IsOnlyFullReturnPossible')
        self.order_item_customers = get_array(json_data.get('OrderItemCustomers'), RailwayOrderItemCustomerInfo)
        self.order_item_blanks = get_array(json_data.get('OrderItemBlanks'), RailwayOrderItemBlankInfo)
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.origin_location_code = json_data.get('OriginLocationCode')
        self.origin_location_name = json_data.get('OriginLocationName')
        self.destination_location_code = json_data.get('DestinationLocationCode')
        self.destination_location_name = json_data.get('DestinationLocationName')
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.previous_order_item_id = get_item(json_data.get('PreviousOrderItemId'), int)
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.pos_sys_name = json_data.get('PosSysName')
        self.amount = get_item(json_data.get('Amount'), float)
        self.reservation_number = json_data.get('ReservationNumber')
        self.operation_type = json_data.get('OperationType')
        self.simple_operation_status = json_data.get('SimpleOperationStatus')
        self.detailed_operation_status = json_data.get('DetailedOperationStatus')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.create_date_time = get_datetime(json_data.get('CreateDateTime'))
        self.confirm_time_limit = get_datetime(json_data.get('ConfirmTimeLimit'))
        self.confirm_date_time = get_datetime(json_data.get('ConfirmDateTime'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.provider_payment_form = json_data.get('ProviderPaymentForm')
        self.is_externally_loaded = get_bool_item(json_data.get('IsExternallyLoaded'))

        self.json_data = json_data


class RailwayShortOrderItemBlankInfo(object):
    def __init__(self, json_data):
        self.place_quantity = get_item(json_data.get('PlaceQuantity'), int)
        self.order_item_blank_id = get_item(json_data.get('OrderItemBlankId'), int)
        self.previous_order_item_blank_id = get_item(json_data.get('PreviousOrderItemBlankId'), int)
        self.blank_number = json_data.get('BlankNumber')
        self.amount = get_item(json_data.get('Amount'), float)

        self.json_data = json_data


class RailwayShortOrderItemInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.service_type = json_data.get('ServiceType')
        self.place_quantity = get_item(json_data.get('PlaceQuantity'), int)
        self.order_item_blanks = get_array(json_data.get('OrderItemBlanks'), RailwayShortOrderItemBlankInfo)
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.pos_sys_name = json_data.get('PosSysName')
        self.amount = get_item(json_data.get('Amount'), float)
        self.reservation_number = json_data.get('ReservationNumber')
        self.operation_type = json_data.get('OperationType')
        self.simple_operation_status = json_data.get('SimpleOperationStatus')
        self.detailed_operation_status = json_data.get('DetailedOperationStatus')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.create_date_time = get_datetime(json_data.get('CreateDateTime'))
        self.confirm_time_limit = get_datetime(json_data.get('ConfirmTimeLimit'))
        self.confirm_date_time = get_datetime(json_data.get('ConfirmDateTime'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.provider_payment_form = json_data.get('ProviderPaymentForm')
        self.is_externally_loaded = get_bool_item(json_data.get('IsExternallyLoaded'))

        self.json_data = json_data


class RailwayShortOrderInfo(object):
    def __init__(self, json_data):
        self.order_items = get_array(json_data.get('OrderItems'), RailwayShortOrderItemInfo)
        self.order_id = get_item(json_data.get('OrderId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.contact_phone = json_data.get('ContactPhone')
        self.contact_emails = json_data.get('ContactEmails')
        self.created = get_datetime(json_data.get('Created'))
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.pos_sys_name = json_data.get('PosSysName')

        self.json_data = json_data


class ServiceUpsaleOperationItemResult(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.upsale_order_item_id = get_item(json_data.get('UpsaleOrderItemId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.is_succeeded = get_bool_item(json_data.get('IsSucceeded'))

        self.json_data = json_data


class CustomerUpsaleOperationResult(object):
    def __init__(self, json_data):
        self.order_customer_id = get_item(json_data.get('OrderCustomerId'), int)
        self.items = get_array(json_data.get('Items'), ServiceUpsaleOperationItemResult)

        self.json_data = json_data


class GeoPoint(object):
    def __init__(self, json_data):
        self.latitude = json_data.get('Latitude')
        self.longitude = json_data.get('Longitude')

        self.json_data = json_data


class TransportNode(object):
    def __init__(self, json_data):
        self.transport_node_id = json_data.get('TransportNodeId')
        self.country_id = json_data.get('CountryId')
        self.region_id = json_data.get('RegionId')
        self.city_id = json_data.get('CityId')
        self.code = json_data.get('Code')
        self.name_ru = json_data.get('NameRu')
        self.name_en = json_data.get('NameEn')
        self.type = json_data.get('Type')
        self.popularity_index = json_data.get('PopularityIndex')
        self.description = json_data.get('Description')
        self.is_active = json_data.get('IsActive')
        self.is_visible = json_data.get('IsVisible')
        self.updated = get_datetime(json_data.get('Updated'))
        self.utc_time_offset = json_data.get('UtcTimeOffset')
        self.location = get_item(json_data.get('Location'), GeoPoint)

        self.json_data = json_data


class City(object):
    def __init__(self, json_data):
        self.city_id = json_data.get('CityId')
        self.country_id = json_data.get('CountryId')
        self.region_id = json_data.get('RegionId')
        self.sys_code = json_data.get('SysCode')
        self.express_code = json_data.get('ExpressCode')
        self.code = json_data.get('Code')
        self.name_ru = json_data.get('NameRu')
        self.name_en = json_data.get('NameEn')
        self.popularity_index = json_data.get('PopularityIndex')
        self.is_active = json_data.get('IsActive')
        self.updated = get_datetime(json_data.get('Updated'))

        self.json_data = json_data


class Country(object):
    def __init__(self, json_data):
        self.country_id = json_data.get('CountryId')
        self.alpha2_code = json_data.get('Alpha2Code')
        self.name_ru = json_data.get('NameRu')
        self.name_en = json_data.get('NameEn')
        self.is_active = json_data.get('IsActive')
        self.updated = get_datetime(json_data.get('Updated'))

        self.json_data = json_data


class Region(object):
    def __init__(self, json_data):
        self.region_id = json_data.get('RegionId')
        self.country_id = json_data.get('CountryId')
        self.iso_code = json_data.get('IsoCode')
        self.name_ru = json_data.get('NameRu')
        self.name_en = json_data.get('NameEn')
        self.is_active = json_data.get('IsActive')
        self.updated = get_datetime(json_data.get('Updated'))

        self.json_data = json_data


class AgentAccount(object):
    def __init__(self, json_data):
        self.current_balance = json_data.get('CurrentBalance')
        self.account_name = json_data.get('AccountName')

        self.json_data = json_data


class RailwayCompensationInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.event = json_data.get('Event')
        self.compensation = json_data.get('Compensation')

        self.json_data = json_data


class RailwayProductPricingInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.compensations = get_array(json_data.get('Compensations'), RailwayCompensationInfo)
        self.package = json_data.get('Package')
        self.compensation = json_data.get('Compensation')
        self.amount = json_data.get('Amount')

        self.json_data = json_data


class RailwayPricingInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.product_pricing_info_list = get_array(json_data.get('ProductPricingInfoList'), RailwayProductPricingInfo)
        self.supplier = json_data.get('Supplier')

        self.json_data = json_data


class RailwayPricingResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.product_pricing_info_list = get_array(json_data.get('ProductPricingInfoList'), RailwayProductPricingInfo)
        self.pricing_info_list = get_array(json_data.get('PricingInfoList'), RailwayPricingInfo)

        self.json_data = json_data


class RaceInfo(object):
    def __init__(self, json_data):
        self.race_id = json_data.get('RaceId')
        self.race_name = json_data.get('RaceName')
        self.free_place_quantity = json_data.get('FreePlaceQuantity')

        self.json_data = json_data


class TariffPriceInfoResponse(object):
    def __init__(self, json_data):
        self.document_types = json_data.get('DocumentTypes')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.tariff_id = json_data.get('TariffId')
        self.tariff_name = json_data.get('TariffName')
        self.tariff_type = json_data.get('TariffType')
        self.route_name = json_data.get('RouteName')
        self.description = json_data.get('Description')
        self.price = json_data.get('Price')
        self.max_tickets_quantity_allowed_for_booking = json_data.get('MaxTicketsQuantityAllowedForBooking')
        self.is_for_guaranteed_seats = json_data.get('IsForGuaranteedSeats')
        self.races = get_array(json_data.get('Races'), RaceInfo)


class AeroexpressConfirmResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.reservation_number = json_data.get('ReservationNumber')
        self.return_till = json_data.get('ReturnTill')
        self.order_item_id = json_data.get('OrderItemId')
        self.amount = json_data.get('Amount')
        self.fare = json_data.get('Fare')
        self.tax = json_data.get('Tax')
        self.confirmed = json_data.get('Confirmed')
        self.void_till = json_data.get('VoidTill')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.order_item_customers = get_array(json_data.get('OrderItemCustomers'), OrderItemCustomerResponseBase)
        self.warnings = get_array(json_data.get('Warnings'), ApiErrorResult)
        self.error_result = get_item(json_data.get('ErrorResult'), ApiErrorResult)


class AeroexpressReturnBlankResponse(object):
    def __init__(self, json_data):
        self.purchase_order_item_blank_id = json_data.get('PurchaseOrderItemBlankId')
        self.return_order_item_blank_id = json_data.get('ReturnOrderItemBlankId')
        self.amount = json_data.get('Amount')

        self.json_data = json_data


class AeroexpressAutoReturnResponse(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.blanks = get_array(json_data.get('Blanks'), AeroexpressReturnBlankResponse)
        self.amount = json_data.get('Amount')
        self.fare = json_data.get('Fare')
        self.tax = json_data.get('Tax')
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.return_order_item_id = json_data.get('ReturnOrderItemId')
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class AeroexpressOrderItemBlankInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.tariff_type = json_data.get('TariffType')
        self.order_item_blank_id = json_data.get('OrderItemBlankId')
        self.previous_order_item_blank_id = json_data.get('PreviousOrderItemBlankId')
        self.blank_number = json_data.get('BlankNumber')
        self.amount = json_data.get('Amount')

        self.json_data = json_data


class AeroexpressOrderItemCustomerInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.order_item_blank_id = json_data.get('OrderItemBlankId')
        self.order_customer_id = json_data.get('OrderCustomerId')
        self.order_item_customer_id = json_data.get('OrderItemCustomerId')
        self.amount = json_data.get('Amount')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)

        self.json_data = json_data


class AeroexpressFullOrderItemInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.order_item_customers = get_array(json_data.get('OrderItemCustomers'), AeroexpressOrderItemCustomerInfo)
        self.order_item_blanks = get_array(json_data.get('OrderItemBlanks'), AeroexpressOrderItemBlankInfo)
        self.arrival_date_time = get_datetime(json_data.get('ArrivalDateTime'))
        self.origin_location_code = json_data.get('OriginLocationCode')
        self.origin_location_name = json_data.get('OriginLocationName')
        self.destination_location_code = json_data.get('DestinationLocationCode')
        self.destination_location_name = json_data.get('DestinationLocationName')
        self.order_id = json_data.get('OrderId')
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.order_item_id = json_data.get('OrderItemId')
        self.pos_sys_name = json_data.get('PosSysName')
        self.amount = json_data.get('Amount')
        self.reservation_number = json_data.get('ReservationNumber')
        self.operation_type = json_data.get('OperationType')
        self.simple_operation_status = json_data.get('SimpleOperationStatus')
        self.detailed_operation_status = json_data.get('DetailedOperationStatus')
        self.departure_date_time = get_datetime(json_data.get('DepartureDateTime'))
        self.create_date_time = get_datetime(json_data.get('CreateDateTime'))
        self.confirm_time_limit = get_datetime(json_data.get('ConfirmTimeLimit'))
        self.confirm_date_time = get_datetime(json_data.get('ConfirmDateTime'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.provider_payment_form = json_data.get('ProviderPaymentForm')
        self.is_externally_loaded = json_data.get('IsExternallyLoaded')


class AeroexpressShortOrderItemInfo(object):
    def __init__(self, json_data):
        self.type = json_data.get('$type')
        self.order_id = json_data.get('OrderId')
        self.agent_reference_id = json_data.get('AgentReferenceId')
        self.order_item_id = json_data.get('OrderItemId')
        self.pos_sys_name = json_data.get('PosSysName')
        self.amount = json_data.get('Amount')
        self.reservation_number = json_data.get('ReservationNumber')
        self.operation_type = json_data.get('OperationType')
        self.simple_operation_status = json_data.get('SimpleOperationStatus')
        self.detailed_operation_status = json_data.get('DetailedOperationStatus')
        self.departure_date_time =  get_datetime(json_data.get('DepartureDateTime'))
        self.create_date_time = get_datetime(json_data.get('CreateDateTime'))
        self.confirm_time_limit =  get_datetime(json_data.get('ConfirmTimeLimit'))
        self.confirm_date_time =  get_datetime(json_data.get('ConfirmDateTime'))
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.provider_payment_form = json_data.get('ProviderPaymentForm')
        self.is_externally_loaded = json_data.get('IsExternallyLoaded')

        self.json_data = json_data


class AeroexpressShortOrderInfo(object):
    def __init__(self, json_data):
        self.order_items = get_array(json_data.get('OrderItems'), AeroexpressShortOrderItemInfo)
        self.order_id = json_data.get('OrderId')
        self.amount = json_data.get('Amount')
        self.contact_phone = json_data.get('ContactPhone')
        self.contact_emails = json_data.get('ContactEmails')
        self.created = get_datetime(json_data.get('Created'))
        self.confirmed = get_datetime(json_data.get('Confirmed'))
        self.pos_sys_name = json_data.get('PosSysName')

        self.json_data = json_data
