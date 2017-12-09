from onelya_railway_sdk.utils import get_array, get_item

from onelya_railway_sdk.wrapper import (FeeCalculation, TrainPriceInfo, StationClarifying, TrainInfo, Route,
                                        CarPriceInfo, ScheduleInfo, TrainRouteRoute, TrainPricingResponse,
                                        RouteReferenced, MealOption)


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
        self.client_fee_calculation = json_data.get('ClientFeeCalculation', None)
        self.agent_fee_calculation = json_data.get('AgentFeeCalculation', None)
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
