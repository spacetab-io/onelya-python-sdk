import os
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.wrapper.types import CarGrouping


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.username = os.environ.get('USERNAME', None)
        self.password = os.environ.get('PASSWORD', None)
        self.pos = os.environ.get('POS', None)

    def test_wrong_auth(self):
        self.assertRaises(OnelyaAPIError, lambda:  API('username', 'password', 'pos'))

    # waiting mock
    #def test_railway_train_pricing(self):
        #destination = 2004000
        #api = API(self.username, self.password, self.pos)
        #self.assertTrue(destination == api.railway.search.train_pricing('Москва', destination, datetime.now().strftime('%Y-%m-%dT%X'), 12, 24, CarGrouping.GROUP))

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError(error_data).message_params is None)