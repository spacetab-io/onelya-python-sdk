from .search import Search


class Railway(object):
    def __init__(self, session):
        self.session = session

        self.search = Search(session)


