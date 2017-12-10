from .session import Session
from .search import Search
from .reservation import Reservation


class API(object):
    def __init__(self, username: str, password: str, pos: str):
        self.__session = Session(username, password, pos)
        self.search = Search(self.__session)
        self.reservation = Reservation(self.__session)

    def get_last_response_data(self):
        return self.__session.last_response_data

    def get_last_request_data(self):
        return self.__session.last_request_data



