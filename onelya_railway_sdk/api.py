from .session import Session
from .railway_search import RailwaySearch


class API(object):
    def __init__(self, username: str, password: str, pos: str):
        self.__session = Session(username, password, pos)
        self.railway_search = RailwaySearch(self.__session)

    def get_last_response_data(self):
        return self.__session.last_response_data

    def get_last_request_data(self):
        return self.__session.last_request_data



