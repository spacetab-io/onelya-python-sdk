from datetime import datetime
from onelya_railway_sdk.wrapper.requests import RequestWrapper
from onelya_railway_sdk.wrapper.types import CarGrouping, PricingTariffType, CarType
from .wrapper import TrainPricing, CarPricing, Schedule, TrainRoute, Routes, RoutePricing, SearchMeal

TRAIN_PRICING_METHOD = 'Railway/V1/Search/TrainPricing'
CAR_PRICING_METHOD = 'Railway/V1/Search/CarPricing'
SCHEDULE_METHOD = 'Railway/V1/Search/Schedule'
TRAIN_ROUTE_METHOD = 'Railway/V1/Search/TrainRoute'
ROUTES_METHOD = 'Railway/V1/Search/Routes'
ROUTE_RICING_METHOD = 'Railway/V1/Search/RoutePricing'
SEARCH_MEAL_METHOD = 'Railway/V1/Search/SearchMeal'


class RailwaySearch(object):
    def __init__(self, session):
        self.__request_wrapper = RequestWrapper(session)

    def train_pricing(self, origin: str, destination: str, departure_date: datetime, time_from: int, time_to: int,
                      car_grouping: CarGrouping=CarGrouping.GROUP):
        response = self.__request_wrapper.make_request(TRAIN_PRICING_METHOD, origin=origin, destination=destination,
                                                       car_grouping=car_grouping, time_from=time_from, time_to=time_to,
                                                       departure_date=departure_date)
        return TrainPricing(response)

    def car_pricing(self, origin_code: str, destination_code: str, departure_date: datetime, train_number: str,
                    car_type: CarType=None, tariff_type: PricingTariffType=PricingTariffType.FULL):
        response = self.__request_wrapper.make_request(CAR_PRICING_METHOD, origin_code=origin_code,
                                                       destination_code=destination_code, departure_date=departure_date,
                                                       train_number=train_number, car_type=car_type,
                                                       tariff_type=tariff_type)
        return CarPricing(response)

    def schedule(self, origin: str, destination: str, time_from: int, time_to: int, departure_date: datetime=None):
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