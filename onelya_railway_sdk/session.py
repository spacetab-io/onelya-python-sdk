import json
import requests
from requests.auth import HTTPBasicAuth
from .exceptions import OnelyaAPIError


class Session(object):
    API_URL = 'https://api-test.onelya.ru/'

    def __init__(self, username, password, pos):
        self.pos = pos

        self.username = username
        self.password = password

        self.requests_session = requests.Session()
        self.requests_session.headers['Pos'] = self.pos
        self.requests_session.headers['Content-Encoding'] = 'gzip'
        self.requests_session.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.requests_session.auth = HTTPBasicAuth(self.username, self.password)

        self.last_response_data = None
        self.last_request_data = None

        self.check_auth()

    def make_api_request(self, method, data):
        """Making a request and checking response

        :param method:
        :param data:
        :return: json data or raise OnelyaAPIError
        """
        data = self.__send_api_request(method, data)
        self.last_response_data = data

        if 'Code' in data:
            raise OnelyaAPIError(data)
        return data

    def __send_api_request(self, method, data):
        """Sending request to Onelya

        :param method:
        :param data:
        :return: json data
        """
        url = '{}{}'.format(Session.API_URL, method)
        self.last_request_data = data
        response = self.requests_session.post(url, data=json.dumps(data))
        return response.json()

    def check_auth(self):
        self.make_api_request('Railway/V1/Search/TrainPricing', {})


