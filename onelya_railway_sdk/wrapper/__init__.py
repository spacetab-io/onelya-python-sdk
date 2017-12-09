from onelya_railway_sdk.utils import get_array


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
        self.departure_date_time = json_data.get('DepartureDateTime', None)
        self.arrival_date_time = json_data.get('ArrivalDateTime', None)
        self.arrival_date_times = json_data.get('ArrivalDateTimes', None)
        self.departure_date_from_forming_station = json_data.get('DepartureDateFromFormingStation', None)
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
        self.arrival_date_time = json_data.get('ArrivalDateTime', None)
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
        self.departure_date_time = json_data.get('DepartureDateTime', None)
        self.arrival_date_time = json_data.get('ArrivalDateTime', None)
        self.arrival_date_times = json_data.get('ArrivalDateTimes', None)
        self.departure_date_from_forming_station = json_data.get('DepartureDateFromFormingStation', None)
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
        self.start_sales_date_time = json_data.get('StartSalesDateTime', None)

        self.json_data = json_data

