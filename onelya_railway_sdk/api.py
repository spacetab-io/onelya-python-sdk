from .session import Session
from .railway import Railway

__version__ = 0.1


class API(object):

    def __init__(self, username, password, pos):
        self.__session = Session(username, password, pos)
        self.railway = Railway(self.__session)

    def get_last_response_data(self):
        return self.__session.last_response_data

    def get_last_request_data(self):
        return self.__session.last_request_data



