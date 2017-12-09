import os
import json
import mock
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.wrapper.types import CarGrouping, PricingTariffType
from onelya_railway_sdk.railway.search import TrainPricing, TrainPriceInfo, Schedule


class MockSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None):
        self.mock_json = json.loads(open('tests/data/{}.json'.format(url[url.index('.ru/') + len('.ru/'):].replace('/V1', '')), 'r', encoding='utf8').read())
        return self

    def json(self):
        return self.mock_json


class MockWrongAUthSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None):
        self.mock_json = {'Code': 12, 'Message': 'Доступ запрещен', 'MessageParam': None}
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

    @mock.patch('requests.Session', MockWrongAUthSession)
    def test_wrong_auth(self):
        self.assertRaises(OnelyaAPIError, lambda:  API('username', 'password', 'pos'))

    @mock.patch('requests.Session', MockSession)
    def test_railway_train_pricing(self):
        api = API(self.username, self.password, self.pos)
        self.assertTrue(self.destination == api.railway.search.train_pricing('Москва', self.destination, datetime.now().strftime('%Y-%m-%dT%X'), 12, 24, CarGrouping.GROUP).destination_station_code)

    @mock.patch('requests.Session', MockSession)
    def test_railway_car_pricing(self):
        api = API(self.username, self.password, self.pos)
        self.assertTrue(self.empty_destination == api.railway.search.car_pricing('2000000', self.empty_destination, datetime.now().strftime('%Y-%m-%dT%X'), '054Ч', None, PricingTariffType.FULL).destination_code)

    @mock.patch('requests.Session', MockSession)
    def test_railway_schedule(self):
        api = API(self.username, self.password, self.pos)
        self.assertTrue(self.destination == api.railway.search.schedule('2000000', self.destination, None, 12, 24).destination_station_code)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError(error_data).message_params is None)

    def test_empty_json_for_train_pricing(self):
        self.assertTrue(TrainPricing({}).json_data == {})

    def test_empty_json_for_train_price_info(self):
        self.assertTrue(TrainPriceInfo({}).json_data == {})

    def test_empty_json_for_schedule(self):
        self.assertTrue(Schedule({}).json_data == {})