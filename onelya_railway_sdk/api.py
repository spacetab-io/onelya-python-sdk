from .info import Info
from .search import Search
from .session import Session
from .utils import get_array
from .wrapper import AgentAccount
from .references import References
from .reservation import Reservation
from .wrapper.requests import RequestWrapper


class API(object):
    def __init__(self, username: str, password: str, pos: str):
        self.__session = Session(username, password, pos)
        self.__request_wrapper = RequestWrapper(self.__session)
        self.search = Search(self.__request_wrapper)
        self.reservation = Reservation(self.__request_wrapper)
        self.info = Info(self.__request_wrapper)
        self.references = References(self.__request_wrapper)

    def balances(self):
        response = self.__request_wrapper.make_request('Partner/V1/Info/Balances')
        return Balances(response)

    @property
    def last_response(self):
        return self.__session.last_response_data
    
    @property
    def last_request(self):
        return self.__session.last_request_data


class Balances(object):
    def __init__(self, json_data):
        self.account_balances = get_array(json_data.get('AccountBalances', None), AgentAccount)

        self.json_data = json_data
