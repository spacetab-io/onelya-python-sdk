import os
import json
import mock
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.railway.search import TrainPricing, TrainPriceInfo, Schedule
from onelya_railway_sdk.wrapper.types import CarGrouping, PricingTariffType, CarType


class MockSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None, timeout=None):
        self.mock_json = json.loads(open('tests/data/{}.json'.format(url[url.index('.ru/') + len('.ru/'):].replace('/V1', '')), 'r', encoding='utf8').read())
        return self

    def json(self):
        return self.mock_json


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.username = os.environ.get('USERNAME', None)
        self.password = os.environ.get('PASSWORD', None)
        self.pos = os.environ.get('POS', None)

        self.destination = '2004000'
        self.empty_destination = None

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_train_pricing(self):
        api = API(self.username, self.password, self.pos)
        train_pricing = api.railway.search.train_pricing('Москва', self.destination, datetime.now(), 12, 24, CarGrouping.GROUP)

        self.assert_json_with_class(train_pricing)

        self.assertTrue(self.destination == train_pricing.destination_station_code)

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_car_pricing(self):
        api = API(self.username, self.password, self.pos)
        car_pricing = api.railway.search.car_pricing('2000000', self.empty_destination, datetime.now(), '054Ч', None, PricingTariffType.FULL)

        self.assert_json_with_class(car_pricing)

        self.assertTrue(self.empty_destination == car_pricing.destination_code)

    @mock.patch('requests.Session', MockSession)
    def test_railway_schedule(self):
        api = API(self.username, self.password, self.pos)
        schedule = api.railway.search.schedule('2000000', self.destination, None, 12, 24)
        self.assert_json_with_class(schedule)

        self.assertTrue(self.destination == schedule.destination_station_code)

    @mock.patch('requests.Session', MockSession)
    def test_train_route(self):
        api = API(self.username, self.password, self.pos)
        train_route = api.railway.search.train_route('054', 'Москва', '2004000', datetime.now())
        self.assert_json_with_class(train_route)

        self.assertEquals(type(train_route.routes), list)

    @mock.patch('requests.Session', MockSession)
    def test_rotes(self):
        api = API(self.username, self.password, self.pos)
        routes = api.railway.search.routes('2000000', '2004000', datetime.now(), 60, 360, True)
        self.assert_json_with_class(routes)

        self.assertEquals(type(routes.routes), list)

    @mock.patch('requests.Session', MockSession)
    def test_rote_pricing(self):
        api = API(self.username, self.password, self.pos)
        rote_pricing = api.railway.search.route_pricing('2000000', '2078750', datetime.now())
        self.assert_json_with_class(rote_pricing)

        self.assertEquals(type(rote_pricing.routes), list)

    @mock.patch('requests.Session', MockSession)
    def test_rote_pricing(self):
        api = API(self.username, self.password, self.pos)
        search_meal = api.railway.search.search_meal(CarType.UNKNOWN, 'sample string 1', 'sample string 2', datetime.now(), 'sample string 4')
        self.assert_json_with_class(search_meal)

        self.assertEquals(type(search_meal.meal_options), list)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError(error_data).message_params is None)

    def test_empty_json_for_train_pricing(self):
        self.assertTrue(TrainPricing({}).json_data == {})

    def test_empty_json_for_train_price_info(self):
        self.assertTrue(TrainPriceInfo({}).json_data == {})

    def test_empty_json_for_schedule(self):
        self.assertTrue(Schedule({}).json_data == {})

    @staticmethod
    def get_var_name(json_key):
        var_name = json_key
        var_name = (var_name[0].lower() if var_name[0].isupper() else var_name[0]) + var_name[1:]
        var_name = ''.join([item if not item.isupper() else ('_%s' % item.lower()) for item in var_name])
        return var_name

    def assert_json_with_class(self, wrapper):
        for key in wrapper.json_data.keys():
            var = wrapper.__getattribute__(self.get_var_name(key))
            if type(var) not in(bool, int, str, type(None)):
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
            if type(data_item) is not dict:
                value = self.get_value(data_item)
                self.assertTrue(value == data_item)
            else:
                for key in data_item.keys():
                    var = var_item.__getattribute__(self.get_var_name(key))
                    if type(var) is list:
                        self.check_data_with_list(var, data_item[key])
                    elif type(var) is dict:
                        self.assertTrue(data_item[key] == var)
                    else:
                        value = self.get_value(var)
                        self.assertTrue(data_item[key] == value)

    def get_value(self, var):
        value = var
        if type(value) == datetime:
            value = value.strftime('%Y-%m-%dT%X')
        return value
