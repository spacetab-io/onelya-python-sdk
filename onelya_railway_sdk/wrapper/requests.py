

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


