import os
import json
import mock
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.railway_search import TrainPricing, TrainPriceInfo, Schedule
from onelya_railway_sdk.reservation.requests import (OrderFullCustomerRequest, RailwayReservationRequest,
                                                     RailwayPassengerRequest)
from onelya_railway_sdk.wrapper.types import (CarType, DocumentType, Sex, CabinGenderKind, AdditionalPlaceRequirements,
                                              CarGrouping, CarStorey, CabinPlaceDemands, ProviderPaymentForm,
                                              PricingTariffType, RailwayPassengerCategory)


class MockSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None, timeout=None):
        self.mock_json = json.loads(open('tests/data/{}.json'.format(url[url.index('.ru/') + len('.ru/'):].
                                                                     replace('/V1', '')), 'r', encoding='utf8').read())
        return self

    def json(self):
        return self.mock_json


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.datetime = datetime.fromtimestamp(0).replace(hour=3)

        self.username = os.environ.get('USERNAME', None)
        self.password = os.environ.get('PASSWORD', None)
        self.pos = os.environ.get('POS', None)

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_train_pricing(self):
        api = API(self.username, self.password, self.pos)
        train_pricing = api.railway_search.train_pricing('Москва', '2004000', self.datetime, 12, 24, CarGrouping.GROUP)

        input_data = json.loads(open('tests/data/Railway/Search/TrainPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(train_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_car_pricing(self):
        api = API(self.username, self.password, self.pos)
        car_pricing = api.railway_search.car_pricing('2000000', '2004000', self.datetime, '054Ч', None, PricingTariffType.FULL)

        input_data = json.loads(open('tests/data/Railway/Search/CarPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(car_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_railway_schedule(self):
        api = API(self.username, self.password, self.pos)
        schedule = api.railway_search.schedule('Москва', '2004000', 12, 24)

        input_data = json.loads(open('tests/data/Railway/Search/Schedule.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(schedule)

    @mock.patch('requests.Session', MockSession)
    def test_train_route(self):
        api = API(self.username, self.password, self.pos)
        train_route = api.railway_search.train_route('054', 'Москва', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/TrainRoute.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(train_route)

    @mock.patch('requests.Session', MockSession)
    def test_rotes(self):
        api = API(self.username, self.password, self.pos)
        routes = api.railway_search.routes('2000000', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/Routes.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(routes)

    @mock.patch('requests.Session', MockSession)
    def test_rote_pricing(self):
        api = API(self.username, self.password, self.pos)
        rote_pricing = api.railway_search.route_pricing('2000000', '2078750', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/RoutePricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(rote_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_search_meal(self):
        api = API(self.username, self.password, self.pos)
        search_meal = api.railway_search.search_meal(CarType.UNKNOWN, 'sample string 1', 'sample string 2',
                                                     'sample string 4', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/SearchMeal.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(search_meal)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_create(self):
        api = API(self.username, self.password, self.pos)

        customers = OrderFullCustomerRequest("4601123450", DocumentType.RUSSIAN_PASSPORT, 'Иван', 'Иванов',
                                             Sex.MALE, 1, 'Иванович', None, 'RU', None, self.datetime)

        passengers = [RailwayPassengerRequest(RailwayPassengerCategory.ADULT, 1, is_invalid=False)]

        reservation_items = RailwayReservationRequest('2006004', '2004001', self.datetime, '054Ч',
                                                      CarType.LUXURY, passengers, 1, '07', 1, 0, CabinGenderKind.NO_VALUE,
                                                      CarStorey.NO_VALUE, (1, 5), None, CabinPlaceDemands.NO_VALUE,
                                                      True, '1Л', AdditionalPlaceRequirements.NO_VALUE, None,
                                                      ProviderPaymentForm.CARD, None, None)

        create = api.railway_reservation.create([customers], [reservation_items], '+79123456789', ['test@test.ru'])

        input_data = json.loads(open('tests/data/Railway/Reservation/Create.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.get_last_request_data())
        self.assert_json_with_class(create)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError('Test/Test', error_data, {}).message_params is None)

    def test_empty_json_for_train_pricing(self):
        self.assertTrue(TrainPricing({}).json_data == {})

    def test_empty_json_for_train_price_info(self):
        self.assertTrue(TrainPriceInfo({}).json_data == {})

    def test_empty_json_for_schedule(self):
        self.assertTrue(Schedule({}).json_data == {})

    def assert_json_with_class(self, wrapper):
        for key in wrapper.json_data.keys():
            var = wrapper.__getattribute__(self.get_var_name(key))
            if type(var) not in(bool, int, float, datetime, str, type(None)):
                if type(var) is list:
                    self.check_data_with_list(var, wrapper.json_data[key])
                elif type(var) is dict:
                    self.assertTrue(wrapper.json_data[key] == var)
                else:
                    self.assertTrue(var.json_data == wrapper.json_data[key])
            else:
                value = self.get_value(var)
                self.assertTrue(wrapper.json_data[key] == value)

    def check_data_with_list(self, wrapper_array, data):
        for var_item, data_item in zip(wrapper_array, data):
            if type(data_item) not in [dict, list]:
                value = self.get_value(data_item)
                self.assertTrue(value == data_item)
            else:
                for key in data_item.keys():
                    var = var_item.__getattribute__(self.get_var_name(key))
                    if type(var) not in (bool, int, float, datetime, str, type(None)):
                        if type(var) is list:
                            self.check_data_with_list(var, data_item[key])
                        elif type(var) is dict:
                            self.assertTrue(data_item[key] == var)
                        else:
                            self.assertTrue(var.json_data == data_item[key])
                    else:
                        value = self.get_value(var)
                        self.assertTrue(data_item[key] == value)

    @staticmethod
    def get_var_name(json_key):
        var_name = json_key
        var_name = (var_name[0].lower() if var_name[0].isupper() else var_name[0]) + var_name[1:]
        var_name = ''.join([item if not item.isupper() else ('_%s' % item.lower()) for item in var_name])
        return var_name.replace('$', '')

    @staticmethod
    def get_value(var):
        value = var
        if type(value) == datetime:
            value = value.strftime('%Y-%m-%dT%X')
        return value
