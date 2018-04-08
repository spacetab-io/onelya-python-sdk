from datetime import datetime
from onelya_sdk.utils import get_array
from onelya_sdk.wrapper.types import TransportNodeType
from onelya_sdk.wrapper import TransportNode, City, Country, Region

TRANSPORT_NODES_METHOD = 'Info/V1/References/TransportNodes'
CITIES_METHOD = 'Info/V1/References/Cities'
COUNTRIES_METHOD = 'Info/V1/References/Countries'
REGIONS_METHOD = 'Info/V1/References/Regions'


class References(object):
    def __init__(self, request_wrapper):
        self.__request_wrapper = request_wrapper

    def transport_nodes(self, last_updated: datetime=None, type: TransportNodeType=None):
        response = self.__request_wrapper.make_request(TRANSPORT_NODES_METHOD, last_updated=last_updated, type=type)
        return TransportNodes(response)

    def cities(self, last_updated: datetime=None):
        response = self.__request_wrapper.make_request(CITIES_METHOD, last_updated=last_updated)
        return Cities(response)

    def countries(self, last_updated: datetime=None):
        response = self.__request_wrapper.make_request(COUNTRIES_METHOD, last_updated=last_updated)
        return Countries(response)

    def regions(self, last_updated: datetime=None):
        response = self.__request_wrapper.make_request(REGIONS_METHOD, last_updated=last_updated)
        return Regions(response)


class TransportNodes(object):
    def __init__(self, json_data):
        self.transport_nodes = get_array(json_data.get('TransportNodes'), TransportNode)

        self.json_data = json_data


class Cities(object):
    def __init__(self, json_data):
        self.cities = get_array(json_data.get('Cities'), City)

        self.json_data = json_data


class Countries(object):
    def __init__(self, json_data):
        self.countries = get_array(json_data.get('Countries'), Country)

        self.json_data = json_data


class Regions(object):
    def __init__(self, json_data):
        self.regions = get_array(json_data.get('Regions'), Region)

        self.json_data = json_data
