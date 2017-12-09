

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


class CarPricingReq(object):
    METHOD = 'Railway/V1/Search/CarPricing'

    def __init__(self, session, origin_code, destination_code, departure_date, train_number, car_type, tariff_type):
        self.session = session

        self.origin_code = origin_code
        self.destination_code = destination_code
        self.departure_date = departure_date
        self.train_number = train_number
        self.car_type = car_type
        self.tariff_type = tariff_type

    def get(self):
        json_data = {
                "OriginCode": self.origin_code,
                "DestinationCode": self.destination_code,
                "DepartureDate": self.departure_date,
                "TrainNumber": self.train_number,
                "CarType": self.car_type,
                "TariffType": self.tariff_type
        }
        return self.session.make_api_request(CarPricingReq.METHOD, json_data)


class ScheduleReq(object):
    METHOD = 'Railway/V1/Search/Schedule'

    def __init__(self, session, origin, destination, departure_date, time_from, time_to):
        self.session = session
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.time_from = time_from
        self.time_to = time_to

    def get(self):
        json_data = {
                "Origin": self.origin,
                "Destination": self.destination,
                "DepartureDate": self.departure_date,
                "TimeFrom": self.time_from,
                "TimeTo": self.time_to
        }
        return self.session.make_api_request(ScheduleReq.METHOD, json_data)


class TrainRouteReq(object):
    METHOD = 'Railway/V1/Search/TrainRoute'

    def __init__(self, session, train_number, origin, destination, departure_date):
        self.session = session
        self.train_number = train_number
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date

    def get(self):
        json_data = {
                "TrainNumber": self.train_number,
                "Origin": self.origin,
                "Destination": self.destination,
                "DepartureDate": self.departure_date
        }
        return self.session.make_api_request(TrainRouteReq.METHOD, json_data)


class RoutesReq(object):
    METHOD = 'Railway/V1/Search/Routes'

    def __init__(self, session, origin, destination, departure_date, min_change_time, max_change_time, first_change_only):
        self.session = session
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.min_change_time = min_change_time
        self.max_change_time = max_change_time
        self.first_change_only = first_change_only

    def get(self):
        json_data = {
                "Origin": self.origin,
                "Destination": self.destination,
                "DepartureDate": self.departure_date,
                "MinChangeTime": self.min_change_time,
                "MaxChangeTime": self.max_change_time,
                "FirstChangeOnly": self.first_change_only
        }
        return self.session.make_api_request(RoutesReq.METHOD, json_data)


class RoutePricingReq(object):
    METHOD = 'Railway/V1/Search/RoutePricing'

    def __init__(self, session, origin_code, destination_code, departure_date):
        self.session = session

        self.origin_code = origin_code
        self.destination_code = destination_code
        self.departure_date = departure_date

    def get(self):
        json_data = {
                "OriginCode": self.origin_code,
                "DestinationCode": self.destination_code,
                "DepartureDate": self.departure_date
        }
        return self.session.make_api_request(RoutePricingReq.METHOD, json_data)

