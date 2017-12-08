from .types import *


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
        self.min_price = json_data.get('MinPrice', 0)
        self.max_price = json_data.get('MaxPrice', 0)
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
        self.discounts = self.__get_discounts(json_data.get('Discounts', None))
        self.info_request_schema = json_data.get('InfoRequestSchema', None)
        self.total_place_quantity = json_data.get('TotalPlaceQuantity', None)
        self.place_reservation_types = json_data.get('PlaceReservationTypes', None)

    @staticmethod
    def __get_discounts(discounts):
        if discounts is not None:
            return [Discount(item) for item in discounts]
        return None


class Discount(object):
    def __init__(self, json_data):
        self.discount_type = json_data.get('DiscountType', None)
        self.description = json_data.get('Description', None)

        self.json_data = json_data


class FeeCalculation(object):
    def __init__(self, json_data):
        self.charge = json_data.get('Charge', 0)
        self.profit = json_data.get('Profit', 0)

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
