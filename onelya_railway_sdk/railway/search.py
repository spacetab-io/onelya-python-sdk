from onelya_railway_sdk.wrapper import *


class Search(object):

    def __init__(self, session):
        self.session = session

    def train_pricing(self, origin, destination, departure_date, time_from, time_to, car_grouping):
        req = TrainPricingReq(self.session, origin, destination, departure_date, time_from, time_to, car_grouping)
        response = req.get()
        return TrainPricing(response)


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


class TrainPriceInfo(object):
    def __init__(self, json_data):
        self.has_electronic_registration = json_data.get('HasElectronicRegistration', None)
        self.has_dynamic_pricing_cars = json_data.get('HasDynamicPricingCars', None)
        self.has_two_storey_cars = json_data.get('HasTwoStoreyCars', None)
        self.carriers = json_data.get('Carriers', [])
        self.car_groups = self.__get_cars_group_price_info(json_data.get('CarGroups', []))
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

    @staticmethod
    def __get_cars_group_price_info(cars_groups):
        if cars_groups is not None:
            cars = []
            for item in cars_groups:
                cars.append(CarGroupPriceInfo(item))
            return cars
        return None


