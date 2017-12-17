from datetime import datetime
from onelya_sdk.utils import get_array, get_item
from onelya_sdk.wrapper.types import CarGrouping, PricingTariffType, CarType
from onelya_sdk.wrapper import (FeeCalculation, TrainPriceInfo, StationClarifying, TrainInfo, Route,
                                CarPriceInfo, ScheduleInfo, TrainRouteRoute, TrainPricingResponse,
                                RouteReferenced, MealOption)

TRAIN_PRICING_METHOD = 'Railway/V1/Search/TrainPricing'
CAR_PRICING_METHOD = 'Railway/V1/Search/CarPricing'
SCHEDULE_METHOD = 'Railway/V1/Search/Schedule'
TRAIN_ROUTE_METHOD = 'Railway/V1/Search/TrainRoute'
ROUTES_METHOD = 'Railway/V1/Search/Routes'
ROUTE_RICING_METHOD = 'Railway/V1/Search/RoutePricing'
SEARCH_MEAL_METHOD = 'Railway/V1/Search/SearchMeal'


class Search(object):
    def __init__(self, request_wrapper):
        self.__request_wrapper = request_wrapper

    def train_pricing(self, origin: str, destination: str, departure_date: datetime, time_from: int=12,
                      time_to: int=24, car_grouping: CarGrouping=CarGrouping.GROUP):
        response = self.__request_wrapper.make_request(TRAIN_PRICING_METHOD, origin=origin, destination=destination,
                                                       car_grouping=car_grouping, time_from=time_from, time_to=time_to,
                                                       departure_date=departure_date)
        return TrainPricing(response)

    def car_pricing(self, origin_code: str, destination_code: str, departure_date: datetime, train_number: str,
                    car_type: CarType=None, tariff_type: PricingTariffType=None):
        response = self.__request_wrapper.make_request(CAR_PRICING_METHOD, origin_code=origin_code,
                                                       destination_code=destination_code, departure_date=departure_date,
                                                       train_number=train_number, car_type=car_type,
                                                       tariff_type=tariff_type)
        return CarPricing(response)

    def schedule(self, origin: str, destination: str, time_from: int=12, time_to: int=24, departure_date: datetime=None):
        response = self.__request_wrapper.make_request(SCHEDULE_METHOD, origin=origin, destination=destination,
                                                       departure_date=departure_date, time_from=time_from,
                                                       time_to=time_to)
        return Schedule(response)

    def train_route(self, train_number: str, origin: str, destination: str, departure_date: datetime):
        response = self.__request_wrapper.make_request(TRAIN_ROUTE_METHOD, train_number=train_number, origin=origin,
                                                       destination=destination, departure_date=departure_date)
        return TrainRoute(response)

    def routes(self, origin: str, destination: str, departure_date: datetime, min_change_time: int=60,
               max_change_time: int=360, first_change_only: bool=True):
        response = self.__request_wrapper.make_request(ROUTES_METHOD, origin=origin, first_change_only=first_change_only,
                                                       departure_date=departure_date, min_change_time=min_change_time,
                                                       max_change_time=max_change_time, destination=destination)
        return Routes(response)

    def route_pricing(self, origin_code: str, destination_code: str, departure_date: datetime):
        response = self.__request_wrapper.make_request(ROUTE_RICING_METHOD, destination_code=destination_code,
                                                       origin_code=origin_code, departure_date=departure_date)
        return RoutePricing(response)

    def search_meal(self, car_type:CarType, carrier_code: str, meal_group: str, country_code: str,
                    departure_date_time: datetime=None):
        response = self.__request_wrapper.make_request(SEARCH_MEAL_METHOD, car_type=car_type, meal_group=meal_group,
                                                       carrier_code=carrier_code, country_code=country_code,
                                                       departure_date_time=departure_date_time)
        return SearchMeal(response)


class TrainPricing(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.trains = get_array(json_data.get('Trains', None), TrainPriceInfo)
        self.departure_time_description = json_data.get('DepartureTimeDescription', None)
        self.arrival_time_description = json_data.get('ArrivalTimeDescription', None)
        self.is_from_ukrain = json_data.get('IsFromUkrain', None)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation', None), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation', None), FeeCalculation)
        self.not_all_trains_returned = json_data.get('NotAllTrainsReturned', None)
        self.station_clarifying = get_item(json_data.get('StationClarifying', None), StationClarifying)
        self.booking_system = json_data.get('BookingSystem', None)
        self.id = json_data.get('Id', None)
        self.route_policy = json_data.get('RoutePolicy', None)

        self.json_data = json_data


class CarPricing(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.cars = get_array(json_data.get('Cars', None), CarPriceInfo)
        self.route_policy = json_data.get('RoutePolicy', None)
        self.train_info = get_item(json_data.get('TrainInfo', None), TrainInfo)
        self.is_from_ukrain = json_data.get('IsFromUkrain', None)
        self.allowed_document_types = json_data.get('AllowedDocumentTypes', None)
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation', None), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation', None), FeeCalculation)
        self.booking_system = json_data.get('BookingSystem', None)

        self.json_data = json_data


class Schedule(object):
    def __init__(self, json_data):
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.route_policy = json_data.get('RoutePolicy', None)
        self.schedules = get_array(json_data.get('Schedules', None), ScheduleInfo)
        self.station_clarifying = get_item(json_data.get('StationClarifying', None), StationClarifying)
        self.not_all_trains_returned = json_data.get('NotAllTrainsReturned', None)

        self.json_data = json_data


class TrainRoute(object):
    def __init__(self, json_data):
        self.routes = get_array(json_data.get('Routes', None), TrainRouteRoute)

        self.json_data = json_data


class Routes(object):
    def __init__(self, json_data):
        self.routes = get_array(json_data.get('Routes', None), Route)

        self.json_data = json_data


class RoutePricing(object):
    def __init__(self, json_data):
        self.train_pricings = get_array(json_data.get('TrainPricings', None), TrainPricingResponse)
        self.routes = get_array(json_data.get('Routes', None), RouteReferenced)
        self.not_all_train_pricings_returned = json_data.get('NotAllTrainPricingsReturned', None)

        self.json_data = json_data


class SearchMeal(object):
    def __init__(self, json_data):
        self.meal_options = get_array(json_data.get('MealOptions', None), MealOption)

        self.json_data = json_data
