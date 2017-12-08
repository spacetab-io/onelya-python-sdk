from .session import Session
from .railway import Railway


class API(object):

    def __init__(self, username, password, pos):
        """Create api object and open session

        Keyword arguments:
            username : str
            password : str
            pos : str -- entry point identifier(from the contract)

        """
        self.session = Session(username, password, pos)
        self.railway = Railway(self.session)
