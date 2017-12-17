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

    def make_api_request(self, method, data):
        response = self.__send_api_request(method, data)
        try:
            response = response.json()
        except ValueError:
            if response.headers['Content-Type'] == 'application/pdf':
                self.last_response_data = response.content
            else:
                self.last_response_data = response.text
            return response

        self.last_response_data = response

        if 'Code' in response:
            raise OnelyaAPIError(method, response, data)
        return response

    def __send_api_request(self, method, data):
        url = '{}{}'.format(Session.API_URL, method)
        self.last_request_data = data
        response = self.requests_session.post(url, data=json.dumps(data), timeout=120)
        return response
