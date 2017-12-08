import os
import json
import mock
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.wrapper.types import CarGrouping


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


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.username = os.environ.get('USERNAME', None)
        self.password = os.environ.get('PASSWORD', None)
        self.pos = os.environ.get('POS', None)

        self.destination = '2004000'

    def test_wrong_auth(self):
        self.assertRaises(OnelyaAPIError, lambda:  API('username', 'password', 'pos'))

    @mock.patch('requests.Session', MockSession)
    def test_railway_train_pricing(self):
        api = API(self.username, self.password, self.pos)
        self.assertTrue(self.destination == api.railway.search.train_pricing('Москва', self.destination, datetime.now().strftime('%Y-%m-%dT%X'), 12, 24, CarGrouping.GROUP).destination_station_code)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError(error_data).message_params is None)