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

        self.__check_auth()

    def make_api_request(self, method, data):
        data = self.__send_api_request(method, data)

        if 'Code' in data:
            raise OnelyaAPIError(data)
        return data

    def __send_api_request(self, method, data):
        url = '{}{}'.format(Session.API_URL, method)
        response = self.requests_session.post(url, data=json.dumps(data))
        return response.json()

    def __check_auth(self):
        self.make_api_request('Info/V1/References/TransportNodes', {})


