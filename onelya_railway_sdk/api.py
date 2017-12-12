from .info import Info
from .search import Search
from .session import Session
from .reservation import Reservation


class API(object):
    def __init__(self, username: str, password: str, pos: str):
        self.__session = Session(username, password, pos)
        self.search = Search(self.__session)
        self.reservation = Reservation(self.__session)
        self.info = Info(self.__session)

    @property
    def last_response(self):
        return self.__session.last_response_data
    
    @property
    def last_request(self):
        return self.__session.last_request_data



