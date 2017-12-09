from onelya_railway_sdk.utils import get_array, get_item
from onelya_railway_sdk.wrapper.requests import TrainPricingReq, CarPricingReq, ScheduleReq
from onelya_railway_sdk.wrapper import (FeeCalculation, TrainPriceInfo, StationClarifying, TrainInfo,
                                        CarPriceInfo, ScheduleInfo)


class Search(object):

    def __init__(self, session):
        self.session = session

    def train_pricing(self, origin, destination, departure_date, time_from, time_to, car_grouping):
        """Getting TrainPricing
        :param origin:
        :param destination:
        :param departure_date:
        :param time_from:
        :param time_to:
        :param car_grouping:
        :return: TrainPricing object
        """
        req = TrainPricingReq(self.session, origin, destination, departure_date, time_from, time_to, car_grouping)
        response = req.get()
        return TrainPricing(response)

    def car_pricing(self, origin_code, destination_code, departure_date, train_number, car_type, tariff_type):
        """Getting CarPricing
        :param origin_code:
        :param destination_code:
        :param departure_date:
        :param train_number:
        :param car_type:
        :param tariff_type:
        :return: CarPricing object
        """
        req = CarPricingReq(self.session, origin_code, destination_code, departure_date, train_number, car_type, tariff_type)
        response = req.get()
        return CarPricing(response)

    def schedule(self, origin, destination, departure_date, time_from, time_to):
        """Getting Schedule
        :param origin:
        :param destination:
        :param departure_date:
        :param time_from:
        :param time_to:
        :return: Schedule object
        """
        req = ScheduleReq(self.session, origin, destination, departure_date, time_from, time_to)
        response = req.get()
        return Schedule(response)


class TrainPricing(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.trains = get_array(json_data.get('Trains', None), TrainPriceInfo)
        self.departure_time_descriptions = json_data.get('DepartureTimeDescriptions', None)
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
        self.not_all_train_returned = json_data.get('NotAllTrainsReturned', None)

        self.json_data = json_data
