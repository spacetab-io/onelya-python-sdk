from datetime import datetime


def get_array(items, item_class=str):
    if type(items) is list:
        return [item_class(item) for item in items]
    return None


def get_array_from_str(items):
    if items not in ['', 'Unknown', 'NoValue', None]:
        if ', ' in items:
            items = items.split(', ')
        else:
            items = items.split(',')
        if all([item.isdigit() for item in items]):
            return [int(item) for item in items]
        return [str(item) for item in items]


def get_item(item, item_class):
    if item is not None:
        return item_class(item)
    return None


def get_datetime(item):
    if item is not None:
        return datetime.strptime(item, '%Y-%m-%dT%X')
    return None


def get_datetime_array(items):
    if items is not None:
        return [datetime.strptime(item, '%Y-%m-%dT%X') for item in items]
    return None


def str_datetime(item):
    if item is not None:
        return item.strftime('%Y-%m-%dT%X')
    return None


def get_bool_item(item):
    if item is not None:
        return bool(item)
    return False
