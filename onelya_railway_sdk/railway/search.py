from onelya_railway_sdk.wrapper import *


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


class TrainPricing(object):
    def __init__(self, json_data):
        self.origin_code = json_data.get('OriginCode', None)
        self.origin_station_code = json_data.get('OriginStationCode', None)
        self.destination_code = json_data.get('DestinationCode', None)
        self.destination_station_code = json_data.get('DestinationStationCode', None)
        self.trains = self.__get_trains_price_info(json_data.get('Trains', None))
        self.departure_time_descriptions = json_data.get('DepartureTimeDescriptions', None)
        self.arrival_time_description = json_data.get('ArrivalTimeDescription', None)
        self.is_from_ukrain = json_data.get('IsFromUkrain', None)
        self.client_fee_calculation = self.__get_fee_calculation(json_data.get('ClientFeeCalculation', None))
        self.agent_fee_calculation = self.__get_fee_calculation(json_data.get('AgentFeeCalculation', None))
        self.not_all_trains_returned = json_data.get('NotAllTrainsReturned', None)
        self.station_clarifying = self.__get_station_clarifying(json_data.get('StationClarifying', None))
        self.booking_system = json_data.get('BookingSystem', None)
        self.id = json_data.get('Id', None)
        self.route_policy = json_data.get('RoutePolicy', None)

        self.json_data = json_data

    def __str__(self):
        return 'TrainPricing: {self.id}'.format(self=self)

    @staticmethod
    def __get_trains_price_info(trains_price_info):
        if trains_price_info is not None:
            trains = []
            for item in trains_price_info:
                trains.append(TrainPriceInfo(item))
            return trains
        return None

    @staticmethod
    def __get_fee_calculation(fee_calcualtion):
        if fee_calcualtion is not None:
            return FeeCalculation(fee_calcualtion)
        return None

    @staticmethod
    def __get_station_clarifying(station_claryfying):
        if station_claryfying is not None:
            return StationClarifying(station_claryfying)
        return None


class TrainPricingReq(object):
    METHOD = 'Railway/V1/Search/TrainPricing'

    def __init__(self, session, origin, destination, departure_date, time_from, time_to, car_grouping):
        self.session = session

        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.time_from = time_from
        self.time_to = time_to
        self.car_grouping = car_grouping

    def get(self):
        json_data = {
                "Origin": self.origin,
                "Destination": self.destination,
                "DepartureDate": self.departure_date,
                "TimeFrom": self.time_from,
                "TimeTo": self.time_to,
                "CarGrouping": self.car_grouping
        }
        return self.session.make_api_request(TrainPricingReq.METHOD, json_data)


