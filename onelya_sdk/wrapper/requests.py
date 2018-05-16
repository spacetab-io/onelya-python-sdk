from datetime import datetime
from ..utils import str_datetime


class RequestWrapper(object):
    def __init__(self, session):
        self.session = session
        self.method_name = None

    def make_request(self, method_name, json=None, **kwargs):
        self.method_name = method_name
        json_data = self.__get_json_data(False, **kwargs) if json is None else json
        return self.session.make_api_request(method_name, json_data)

    def __get_json_data(self, recursive, **kwargs):
        json_data = {}
        for key in kwargs.keys():
            item = kwargs[key]
            onelya_key = self.__get_onelya_key(key)
            if type(item) in [str, int, float, type(None), bool]:
                json_data[onelya_key] = item
            elif type(item) is dict:
                json_data[onelya_key] = self.__get_json_data(False, **item)
            elif type(item) is list:
                json_data[onelya_key] = [self.__get_json_data(True, **{'Key': list_item}) for list_item in item]
            elif type(item) is datetime:
                json_data[onelya_key] = str_datetime(item)
            else:
                object_name = self.__get_onelya_key(key)
                if json_data.get(object_name, None) is None:
                    json_data[object_name] = {}
                for object_attribute in item.__dict__.keys():
                    if object_attribute != 'json_data':
                        object_attribute_name = self.__get_onelya_key(object_attribute)
                        json_data[object_name][object_attribute_name] = \
                            self.__get_json_data(True, **{object_attribute_name: item.__getattribute__(object_attribute)})
            if recursive:
                return json_data[key]
        return json_data

    def __get_onelya_key(self, key):
        """Getting json key
        Also converting type -> $type if method not from references

        :param key:
        :param method_name:
        :return:
        """
        if key == 'type' and 'References' not in self.method_name:
            return '$type'
        new_key = key[0].upper()
        i = 1
        while i < len(key):
            if key[i] == '_':
                new_key += key[i + 1].upper()
                i += 1
            else:
                new_key += key[i]
            i += 1
        return new_key


